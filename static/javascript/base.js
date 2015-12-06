/**
 * Created by SHAAPAOJA on 12/5/2015.
 */

$.fn.stars = function() {
    return $(this).each(function() {
        $(this).html($('<span />').width(Math.max(0, (Math.min(5, parseFloat($(this).html())))) * 32));
    });
};

var SUS = (function() {
    var initConsole = function (release) {
        /**
		 * Protect window.console method calls
		 */
        // Union of Chrome, Firefox, IE, Opera, and Safari console methods
        var methods = ["assert", "cd", "clear", "count", "countReset", "debug", "dir", "dirxml", "error", "exception",
            "group", "groupCollapsed", "groupEnd", "info", "log", "markTimeline", "profile", "profileEnd", "select",
            "table", "time", "timeEnd", "timeStamp", "timeline", "timelineEnd", "trace", "warn"];
        var releaseMethods = ["error", "warn"];
        var console = (window.console = window.console || {});
        var method;
        var noop = function () {
        };

        for (var i = 0; i < methods.length; i++) {
            method = methods[i];

            // define undefined methods as noops to prevent errors
            if (!console[method] || (release && releaseMethods.indexOf(method) == -1)) {
                console[method] = noop;
            }
        }
    };

    var ratingClickHandler = function($this) {
        var $parent = $this.parent();
        var cooldown = $parent.data('cooldown');

        if (cooldown === undefined || !cooldown) {
            console.log('Add rating');
            $.post($this.data('posturl')).done(function(data) {
                console.debug('finished posting');
                console.debug('Got data: ', data);
                var $jqueryStatsText = $parent.siblings('.jqueryStats').children('.jqueryStatsText');
                $jqueryStatsText.children('div').not('.jqueryProductName').each(function(index) {
                    if (index == 0) {
                        $(this).text('Total votes - ' + data['votes']);
                    } else {
                        $(this).text(index + ' stars - ' + ((data['votes_by_star'][index-1]/data['votes']) * 100).toFixed(2) + '%');
                    }
                });
                $parent.data('cooldown', true);
                console.log($this.is(':checked'));

                setTimeout(function() {
                    $parent.find('span.star').each(function(index) {
                        var $star = $(this);
                        $star.text(Math.min(1, data['rating'] - index)).children('span').remove().end().stars();
                    });
                }, 2000);

                setTimeout(function() {
                    $parent.data('cooldown', false);
                }, 5000);
            });
        } else {
            console.log("RELAX!!!");
        }
    };

    return {
        init: function() {
            initConsole(false);
            $('span.star').hover(function() {
                var $this = $(this);
                $this.prevAll().andSelf().each(function() {
                    var $star = $(this);
                    $star.children().hide();
                    $star.addClass('starHover');
                });
            }, function() {
                var $this = $(this);
                $this.prevAll().andSelf().each(function() {
                    var $star = $(this);
                    $star.removeClass('starHover');
                    $star.children().show();
                });
            }).click(function() {
                ratingClickHandler($(this));
            }).stars();
        }
    }
})();

$(function() {
    SUS.init();
});
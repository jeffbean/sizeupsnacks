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

    var cooldownTimerFunction = null;

    var ratingClickHandler = function($this) {
        var $parent = $this.parent();
        var cooldownCount = $parent.data('cooldownCount');
        var COOLDOWN_TIME = 1000;

        console.log("cooldownCount: ", cooldownCount);
        if (cooldownCount === undefined || cooldownCount === -1) {
            $.post($this.data('posturl')).done(function(data) {
                console.debug('finished posting');
                console.debug('Got data: ', data);
                var $jqueryStatsText = $parent.siblings('.jqueryStats').children('.jqueryStatsText');
                $jqueryStatsText.children('div').not('.jqueryProductName').each(function(index) {
                    if (index == 0) {
                        $(this).text('Total votes - ' + data['votes']);
                    } else {
                        $(this).text(6-index + ' stars - ' + ((data['votes_by_star'][5-index]/data['votes']) * 100).toFixed(2) + '%');
                    }
                });
                $parent.data('cooldown', true);
                $parent.siblings('.jqueryThankYou').fadeIn();

                setTimeout(function() {
                    $parent.find('span.star').each(function(index) {
                        var $star = $(this);
                        $star.text(Math.min(1, data['rating'] - index)).children('span').remove().end().stars();
                    });
                    $parent.siblings('.jqueryThankYou').fadeOut();
                }, 2000);

                $parent.data('cooldownCount', 0);

                cooldownTimerFunction = setTimeout(function() {
                    console.log('Cooldown set');
                    $parent.data('cooldownCount', -1);
                }, COOLDOWN_TIME);
            });
        } else {
            var $calmDown = $parent.siblings('.jqueryCalmDown');
            clearTimeout(cooldownTimerFunction);

            $parent.data('cooldownCount', cooldownCount + 1);

            if (cooldownCount + 1 > 100) {
                $calmDown.text('Your cooldown is now ' + Math.round((COOLDOWN_TIME * cooldownCount)/60000) + ' minutes. Good luck waiting for that.');
            } else if (cooldownCount + 1 > 25) {
                $calmDown.text('OK come on now! JUST STOP!');
            } else if (cooldownCount + 1 > 5) {
                $calmDown.text('Wow. You really want to vote!');
            }

            $calmDown.fadeIn();

            var elongatedTimer = COOLDOWN_TIME * (cooldownCount + 1);
            cooldownTimerFunction = setTimeout(function() {
                console.log('Cooldown set');
                $parent.data('cooldownCount', -1);
            }, elongatedTimer);

            setTimeout(function() {
                $parent.siblings('.jqueryCalmDown').fadeOut();
            }, 2000);
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
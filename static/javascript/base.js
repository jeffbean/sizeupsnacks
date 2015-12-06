/**
 * Created by SHAAPAOJA on 12/5/2015.
 */

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
        console.debug("Rating clicked: ", $this);
        console.debug("Rating clicked parent: ", $this.parent());

        var $parent = $this.parent();
        var cooldown = $parent.data('cooldown');

        if (cooldown === undefined || !cooldown) {
            console.log('Add rating');
            $.post($this.data('posturl')).done(function() {
                console.debug('finished posting');
                $parent.data('cooldown', true);
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
            $("input").click(function() {
                ratingClickHandler($(this));
            });
        }
    }
})();

$(function() {
    SUS.init();
});
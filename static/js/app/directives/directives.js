Blog.directive("keepScrollPos", function ($route, $window, $timeout, $location, $anchorScroll) {

    // compile function
    return function (scope, element, attrs) {
        scope.scrollPos = {}; // scroll position of each view
        $(window).on('scroll', function () {
            if (scope.okSaveScroll) { // false between $routeChangeStart and $routeChangeSuccess
                scope.scrollPos[$location.path()] = $(window).scrollTop();
                //console.log($scope.scrollPos);
            }
        });

        scope.scrollClear = function (path) {
            scope.scrollPos[path] = 0;
        };

        scope.$on('$routeChangeStart', function () {
            scope.okSaveScroll = false;
        });

        scope.$on('$routeChangeSuccess', function () {
            $timeout(function () { // wait for DOM, then restore scroll position
                $(window).scrollTop(scope.scrollPos[$location.path()] ? scope.scrollPos[$location.path()] : 0);
                scope.okSaveScroll = true;
            }, 0);
            setTimeout(function () {
                $(".loading-page").hide();
            }, 300);
        });
    }
});

Blog.directive('sideContent', function () {
    return {
        replace: true,
        restrict: 'E',
        templateUrl: "static/js/app/views/side_content.html"
    };
});

Blog.directive('search', function () {
    return function ($scope, element) {
        element.bind("keypress", function (event) {
            var val = element.val();
            if (val.length > 1) {
                $scope.callSearchingPosts(val);
            }
        });
    };
});

Blog.directive('headerAnimate', function ($location) {
    return function (scope, element, attrs) {
        scope.$on('$routeChangeStart', function () {
            if ($location.path().indexOf("/post/") > -1 || $location.path().indexOf("/contact/") > -1 || $location.path().indexOf("/kokoloji/") > -1) {
                element.addClass("toolbar-shadow").removeAttr("style")
            } else {
                element.removeClass("toolbar-shadow").css({
                    background: "transparent"
                })
            }
        });
        angular.element($window).bind("scroll", function () {
            $gd_cover = $("#cover");
            $gd_header = $("#header");
            var scrollTop = $window.scrollTop(),
                gd_cover_height = $gd_cover.height() - $gd_header.height(),
                gd_cover_wrap = (gd_cover_height - scrollTop) / gd_cover_height;
            scrollTop >= gd_cover_height ? $gd_header.addClass("toolbar-shadow").removeAttr("style") : $gd_header.removeClass("toolbar-shadow").css({
                background: "transparent"
            }), $(".cover-wrap").css("opacity", gd_cover_wrap);
        });
    };
});

Blog.directive("randomBackgroundcolor", function () {
    return {
        restrict: 'EA',
        replace: false,
        link: function (scope, element, attr) {

            //generate random color
            var color = '#0288d1';

            //Add random background class to selected element
            element.css('background-color', color);

        }
    }
});
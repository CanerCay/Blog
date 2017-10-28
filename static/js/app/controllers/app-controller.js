Blog.controller('AppController', function ($scope, $rootScope, $location, GlobalService, PostService, AboutService) {

    $scope.globals = GlobalService;
    $scope.initialize = function (is_authenticated, is_superuser) {
        $scope.globals.is_authenticated = is_authenticated;
        $scope.globals.is_superuser = is_superuser;
        GlobalService.get("/config/").then(function (data) {
            $scope.globals.site_config = data;
        });
        AboutService.get().then(function (data) {
            $scope.about = data;
        });

    };
    $scope.scrollTopAnimate = function () {
        $("html, body").animate({scrollTop: $("#main").offset().top - 56}, 500, "linear")
    };

    $scope.callSearchingPosts = function (val) {
        PostService.list("/posts/?search=" + val + "&limit=10").then(function (data) {
            $scope.searchingPosts = data.results;
        });
    }
});

Blog.controller('FeedController', function ($scope, GlobalService, PostService, TagService, posts, popularPosts, lastPosts) {
    $scope.globals = GlobalService;
    $scope.showPagination = true;
    $scope.popularPosts = popularPosts.results;
    $scope.lastPosts = lastPosts.results;
    $scope.posts = posts.results;
    $scope.next = posts.next;
    if ($scope.next == null) {
        $scope.showPagination = false;
    }

    $scope.getNext = function () {
        var $pagination = $("#pagination");
        $pagination.addClass("infinite-scroll").addClass("loanding");
        setTimeout(function () {
            $scope.getPostsPagination();
        }, 500);
    };


    $scope.getPostsPagination = function () {
        console.log($scope.next);
        PostService.list($scope.next).then(function (data) {
            data.next != null ? $scope.next = data.next : $scope.showPagination = false;
            $scope.posts.push.apply($scope.posts, data.results);
        }, function (status) {
            $pagination.removeClass("loanding");
            console.log(status);
        });

    };
});
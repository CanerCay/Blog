Blog.controller('PostController', function ($scope, $routeParams, $location, PostService,
                                            TagService, GlobalService, post, popularPosts, lastPosts ) {
    post_url = "/posts/?";
    $scope.post = post;
    $scope.popularPosts = popularPosts.results;
    $scope.lastPosts = lastPosts.results;
    $scope.globals = GlobalService;

    $scope.getRelatedPosts = function () {
        if($scope.post.tags_details.length != 0)
            PostService.list(post_url + "limit=3" + "&tags__name=" + "deneme%20tag").then(function (data){
                $scope.relatedPosts = data.results;
            });
        else
            PostService.list(post_url + "limit=3").then(function (data){
                $scope.relatedPosts = data.results;
            });
    };
});
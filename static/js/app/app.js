'use strict';

var Blog = angular.module("Blog", ["ngCookies", "ngRoute", "ngtimeago", 'ngSanitize', 'angularFileUpload',
        'chieffancypants.loadingBar'], function ($interpolateProvider) {
        $interpolateProvider.startSymbol("{[{");
        $interpolateProvider.endSymbol("}]}");
    }
);

Blog.run(function ($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    console.log($cookies.get('csrftoken'));
});

Blog.config(function ($routeProvider) {
    var post_url = "/posts/?";
    var limit_filter = "limit=4";
    $routeProvider
        .when("/", {
            templateUrl: "static/js/app/views/feed.html",
            controller: "FeedController",
            resolve: {
                posts: function (PostService) {
                    return PostService.list(post_url);
                },
                popularPosts: function (PostService) {
                    return PostService.list(post_url + limit_filter + "&ordering=-counter");
                },
                lastPosts: function (PostService) {
                    return PostService.list(post_url + limit_filter + "&ordering=-created_on");
                }
            }
        })
        .when("/post/:slug", {
            templateUrl: "static/js/app/views/view.html",
            controller: "PostController",
            resolve: {
                post: function ($route, PostService) {
                    var slug = $route.current.params.slug;
                    return PostService.get(slug);
                },
                popularPosts: function (PostService) {
                    return PostService.list(post_url + limit_filter + "&ordering=-counter");
                },
                lastPosts: function (PostService) {
                    return PostService.list(post_url + limit_filter + "&ordering=-created_on");
                }
            }
        })
        .when("/about/", {
            templateUrl: "static/js/app/views/about.html",
            controller: "AboutController",
            resolve: {
                skill: function (AboutService) {
                    return AboutService.list("/aboutme/skill");
                },
                experience: function (AboutService) {
                    return AboutService.list("/aboutme/experience");
                },
                education: function (AboutService) {
                    return AboutService.list("/aboutme/education");
                },
                project: function (AboutService) {
                    return AboutService.list("/aboutme/project");
                }
            }
        })
        .when("/contact/", {
            templateUrl: "static/js/app/views/contact.html",
            controller: "ContactController"
        })
        .otherwise({
            redirectTo: '/'
        });
});


Blog.factory('PostService', function ($http, $q) {
    var api_url = "/posts/";
    return {
        get: function (slug) {
            var url = api_url + slug + "/";
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        },

        list: function (url) {
            var pagination_url = url != null ? url : api_url;
            var defer = $q.defer();
            $http({method: 'GET', url: pagination_url}).
            success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        },
        save: function (post) {
            var url = api_url;
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: url,
                data: post
            }).
            success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        }
    }
});
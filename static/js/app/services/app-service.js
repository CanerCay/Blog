Blog.factory('GlobalService', function ($http, $q) {
    return {
        is_authenticated: false,
        is_superuser: false,
        get: function (url) {
            var defer = $q.defer();
            $http({method: 'GET', url: url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    defer.reject(status);
                });
            return defer.promise;
        }
    };
});
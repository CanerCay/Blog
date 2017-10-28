Blog.factory('AboutService', function ($http, $q) {
    about_url = "/aboutme/";
	return {
        get: function(){
            var defer = $q.defer();
            $http({method: 'GET', url: about_url}).
                success(function (data, status, headers, config) {
                    defer.resolve(data);
                })
                .error(function (data, status, headers, config) {
                    console.log(data);
                    console.log(status);
                    defer.reject(status);
                });
            return defer.promise;
        },
        list: function(url){
            var pagination_url = url + "?limit=10";
            var defer = $q.defer();
            $http({method: 'GET', url: pagination_url}).
            success(function (data, status, headers, config) {
                defer.resolve(data);
            }).error(function (data, status, headers, config) {
                defer.reject(status);
            });
            return defer.promise;
        }
    };
});
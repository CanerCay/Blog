Blog.factory('ContactService', function ($http, $q) {
    var api_url = "/aboutme/contact/";
    return {
        save: function (contact) {
            var url = api_url;
            var defer = $q.defer();
            $http({
                method: 'POST',
                url: url,
                data: contact
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

/**
 * Created by Caner on 2.09.2016.
 */

Blog.controller('ContactController', function ($scope, $routeParams, $location,
                                               GlobalService, ContactService) {
    $scope.contact = new Object();
    $scope.SendContact = function () {
        $("#ajaxsuccess").hide();
        ContactService.save($scope.contact).then(function (data) {
            console.log(data);
            if (data.data === true) {
                $("#ajaxsuccess").show();
                var rem = document.querySelectorAll("[id*='err-']"), i = 0;
                for (; i < rem.length; i++) {
                    $(rem[i]).hide();
                }
                $scope.contact = new Object();
            } else {
                for (prop in data) {
                    if (data.hasOwnProperty(prop)) {
                        var err = $("#err-" + prop);
                        err.html(data[prop][0]);
                        err.show();
                    }
                }
            }
        }, function (status) {
            console.log(status);
        });

    }
});
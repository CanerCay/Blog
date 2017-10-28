/**
 * Created by Caner on 28.08.2016.
 */

Blog.controller('AboutController', function ($scope, $routeParams, $location,
                                             GlobalService, AboutService, skill, experience, education, project) {
    var mid = parseInt(skill.results.length * 0.5);


    $scope.skills1 = skill.results.slice(0, mid);
    $scope.skills2 = skill.results.slice(mid);
    $scope.experiences = experience.results;
    $scope.educations = education.results;
    $scope.projects = project.results;
});

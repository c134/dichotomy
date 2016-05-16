dichotomy.controller('CreateWorkplaceController', ['$scope', 'WorkPlace', function ($scope, WorkPlace) {
    $scope.workplace = {};
    $scope.workplace.skills = [];
    $scope.removeSkill = function () {
        var _lastItem = $scope.workplace.skills.length - 1;
        $scope.workplace.skills.splice(_lastItem);
    };
    $scope.addSkill = function () {
        var _newItem = $scope.workplace.skills.length + 1;
        $scope.workplace.skills.push({number: _newItem});
    };
    $scope.createWorkplace = function () {
        WorkPlace.save($scope.workplace, function (response) {
            console.log(response);
        }, function (error) {
            console.log(error);
        });
    }
}]);
dichotomy.controller('CalculateDichotomy', ['$scope', '$filter', '$state', 'WorkPlace', 'Dichotomy', function ($scope, $filter, $state, WorkPlace, Dichotomy) {
    WorkPlace.get({id: $state.params.id}).$promise.then(function (response) {
        $scope.workplace = $filter('filter')(response, {model: 'dichotomy.workposition'})[0];
        $scope.workplacesWithSkills = response;
        var _index = $scope.workplacesWithSkills.indexOf($scope.workplace);
        $scope.workplacesWithSkills.splice(_index, 1);
    });
    $scope.calculateDichotomy = function () {
        $scope.workplacesWithSkills.workplace_id = $state.params.id;
        console.log($scope.workplacesWithSkills);
        Dichotomy.save($scope.workplacesWithSkills,function (response) {
            console.log(response);
        }, function (response) {

        });
    };

}]);

dichotomy.controller('WorkplaceOverview', ['$scope', 'WorkPlace', function ($scope, WorkPlace) {
    WorkPlace.all({get_all: 1}).$promise.then(function (response) {
        $scope.workplaces = response;
    });
}]);
dichotomy.config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');
    $stateProvider
       .state('workplace_overview', {
            url: '/workplace_overview',
            templateUrl: '/static/dichotomy/angular-views/workplace_overview.html',
            controller: 'WorkplaceOverview'
        })
        .state('create_workplace', {
            url: '/create-workplace',
            templateUrl: '/static/dichotomy/angular-views/create_workplace.html',
            controller: 'CreateWorkplaceController'
        })
        .state('calculate_dichotomy', {
            url: '/calculate-dichotomy/:id',
            templateUrl: '/static/dichotomy/angular-views/calculate_dichotomy.html',
            controller: 'CalculateDichotomy'
        })
}]);
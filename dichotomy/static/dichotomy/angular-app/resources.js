dichotomy.factory('WorkPlace', function ($resource) {
    return $resource('api/create_workplace/:id/:get_all/', {}, {
        all: {method: "GET", isArray: true, params: {get_all: '@get_all'}},
        get: {method: "GET", isArray: true, params: {id: '@id'}},
        update: {method: 'PUT', params: {id: '@id'}}
    });
});

dichotomy.factory('Dichotomy', function ($resource) {
    return $resource('api/calculate_dichotomy/:id', {} ,{
        all: {method: "GET", isArray: true, params: {get_all: '@get_all'}},
        get: {method: "GET", isArray: true, params: {id: '@id'}},
        update: {method: 'PUT', params: {id: '@id'}}
    });
});
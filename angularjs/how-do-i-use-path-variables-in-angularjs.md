# How do I use path variables in AngularJS?
// plain

Path variables in AngularJS are used to store parameters in the URL. These parameters can be used to pass information to the controller and can be retrieved using the $routeParams service.

## Example code

```
var app = angular.module('myApp', ['ngRoute']);

app.config(function($routeProvider) {
    $routeProvider
        .when('/users/:userId', {
            templateUrl: 'user.html',
            controller: 'UserController'
        });
});

app.controller('UserController', function($scope, $routeParams) {
    $scope.userId = $routeParams.userId;
});
```

In the above example, we define a route with a path variable `userId` and use the `$routeParams` service to get the value of `userId` in the controller.

## Code explanation

* `var app = angular.module('myApp', ['ngRoute']);`: Declares a new AngularJS application.
* `$routeProvider.when('/users/:userId', {...})`: Defines a route with a path variable `userId`.
* `$scope.userId = $routeParams.userId;`: Retrieves the value of `userId` using the `$routeParams` service.

## Helpful links
* [AngularJS $routeParams Service](https://docs.angularjs.org/api/ngRoute/service/$routeParams)
* [AngularJS Routing and Views Tutorial](https://scotch.io/tutorials/angular-routing-using-ui-router)

onelinerhub: [How do I use path variables in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-path-variables-in-angularjs)
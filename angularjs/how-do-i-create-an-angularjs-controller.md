# How do I create an AngularJS controller?
// plain

To create an AngularJS controller, you can use the `.controller` method. This method takes two parameters: the name of the controller and a function that defines the controller's behavior. The controller function can take an optional `$scope` parameter. Here is an example:

```
angular.module('myApp', [])
.controller('myController', function($scope) {
  $scope.message = 'Hello World';
});
```

This will create a controller called `myController` that will set the `message` property of the `$scope` object to `Hello World`.

## Code explanation


1. `angular.module('myApp', [])`: this creates a module called `myApp` with no dependencies.
2. `.controller('myController', function($scope) {...})`: this creates a controller called `myController` with a function that takes an optional `$scope` parameter.
3. `$scope.message = 'Hello World'`: this sets the `message` property of the `$scope` object to `Hello World`.

For more information, see the [AngularJS documentation](https://docs.angularjs.org/guide/controller).

onelinerhub: [How do I create an AngularJS controller?](https://onelinerhub.com/angularjs/how-do-i-create-an-angularjs-controller)
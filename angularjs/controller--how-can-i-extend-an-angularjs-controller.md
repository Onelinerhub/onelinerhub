# controller

How can I extend an AngularJS controller?
// plain

An AngularJS controller can be extended by creating a new controller that is a child of the existing one. This is done by using the `.controller` method with the `parent` argument set to the name of the parent controller.

For example:
```
angular.module('myApp', [])
  .controller('ParentController', function($scope) {
    $scope.greeting = 'Hello';
  })
  .controller('ChildController', function($scope) {
    $scope.name = 'World';
  }, { parent: 'ParentController' });
```

This will create a new controller `ChildController` with `ParentController` as its parent. The `ChildController` will have access to all of the variables and methods of the `ParentController`.

The parts of the code above are:
- `angular.module('myApp', [])` - this defines an AngularJS module named `myApp`
- `.controller('ParentController', function($scope) { ... })` - this defines a controller named `ParentController` with a `$scope` parameter
- `.controller('ChildController', function($scope) { ... }, { parent: 'ParentController' })` - this defines a controller named `ChildController` with a `$scope` parameter and a `parent` argument set to the name of the parent controller

For more information on extending controllers in AngularJS, see the [AngularJS Documentation](https://docs.angularjs.org/guide/controller).

onelinerhub: [controller

How can I extend an AngularJS controller?](https://onelinerhub.com/angularjs/controller--how-can-i-extend-an-angularjs-controller)
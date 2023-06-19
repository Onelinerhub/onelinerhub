# How do I use the AngularJS scope in my application?
// plain

The AngularJS scope is a powerful tool for managing application data and behavior. It is an object that refers to the application model and is available for both the view and the controller.

To use the AngularJS scope in an application, you must first create a scope object in the controller. This can be done by injecting the `$scope` service into the controller:

```
angular.module('myApp', [])
  .controller('MyController', function($scope) {
    // Create the scope object
    $scope.name = 'John Doe';
  });
```

Once the scope object is created, you can use it to bind data and behavior to the view. For example, to bind the `name` property to the view, you can use the `ng-model` directive:

```
<input type="text" ng-model="name">
```

The `name` property will now be available in the view and any changes to it will be reflected in the view.

You can also use the scope object to create custom behavior. For example, to create a function that will be available in the view, you can use the `$scope` object:

```
$scope.sayHello = function() {
  console.log('Hello ' + $scope.name);
};
```

The `sayHello` function can now be used in the view with the `ng-click` directive:

```
<button ng-click="sayHello()">Say Hello</button>
```

When the button is clicked, the `sayHello` function will be called and the output will be `Hello John Doe`.

The AngularJS scope is a powerful tool for managing application data and behavior. For more information, see the [AngularJS documentation](https://docs.angularjs.org/guide/scope).

onelinerhub: [How do I use the AngularJS scope in my application?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-scope-in-my-application)
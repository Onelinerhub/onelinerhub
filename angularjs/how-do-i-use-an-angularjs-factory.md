# How do I use an AngularJS factory?
// plain

An AngularJS factory is a service that can be used to create custom objects and functions. To use an AngularJS factory, you need to first define it in your application module. For example:

```
var app = angular.module('myApp', []);

app.factory('myFactory', function() {
    return {
        getName: function() {
            return 'John Doe';
        }
    }
});
```

You can then inject the factory into your controller or service and use the functions it provides. For example:

```
app.controller('myController', function($scope, myFactory) {
    $scope.name = myFactory.getName();
});
```

The output of this code would be `John Doe`.

## Code explanation


- `var app = angular.module('myApp', []);` - This line defines a new AngularJS application module.
- `app.factory('myFactory', function() {` - This line defines a new factory with the name `myFactory`.
- `return {` - This line returns an object containing all the functions and variables that will be available from the factory.
- `getName: function() {` - This line defines a function called `getName` which will be available from the factory.
- `return 'John Doe';` - This line returns the string `John Doe` when the `getName` function is called.
- `$scope.name = myFactory.getName();` - This line calls the `getName` function from the `myFactory` factory and assigns the returned value to the `$scope.name` variable.

## Helpful links

- [AngularJS Factories](https://docs.angularjs.org/guide/services)
- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/angularjs_factories.htm)

onelinerhub: [How do I use an AngularJS factory?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-factory)
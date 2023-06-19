# How can I use a getter in AngularJS?
// plain

A getter in AngularJS is a function that retrieves a value from a property or object.

Here is an example of a getter in AngularJS:

```
var app = angular.module('myApp', []);

app.controller('myController', function($scope) {
    $scope.name = "John Doe";

    $scope.getName = function() {
        return $scope.name;
    };
});
```

The `getName` function is the getter. It is used to retrieve the value of the `name` property.

To use the getter, you can simply call it like this:

```
var name = $scope.getName();

console.log(name); // Output: "John Doe"
```

The code above will output the value of the `name` property, which is "John Doe".

## Code explanation


- `var app = angular.module('myApp', []);`: This line creates an AngularJS module called `myApp`.
- `app.controller('myController', function($scope) {`: This line creates a controller called `myController`.
- `$scope.name = "John Doe";`: This line sets the `name` property of the `$scope` object to "John Doe".
- `$scope.getName = function() {`: This line creates the `getName` function, which will be used as the getter.
- `return $scope.name;`: This line returns the value of the `name` property.
- `var name = $scope.getName();`: This line calls the `getName` function and stores the returned value in the `name` variable.
- `console.log(name);`: This line outputs the value of the `name` variable.

Here are some ## Helpful links

- [AngularJS Getters](https://docs.angularjs.org/api/ng/type/angular.Module#getter)
- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/)

onelinerhub: [How can I use a getter in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-a-getter-in-angularjs)
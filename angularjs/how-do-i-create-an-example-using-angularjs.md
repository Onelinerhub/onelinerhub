# How do I create an example using AngularJS?
// plain

The following example uses AngularJS to create a simple application that will display a greeting message when a button is clicked.

```
<!DOCTYPE html>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
    <script>
      var app = angular.module('myApp', []);
      app.controller('myCtrl', function($scope) {
        $scope.name = "";
        $scope.greeting = function() {
          alert("Hello " + $scope.name);
        }
      });
    </script>
  </head>
  <body>
    <div ng-app="myApp" ng-controller="myCtrl">
      Name: <input type="text" ng-model="name">
      <button ng-click="greeting()">Greet</button>
    </div>
  </body>
</html>
```

This example creates an AngularJS application with a controller named `myCtrl` that has a single scope variable `name`. The controller also has a function named `greeting` that will display an alert box with a greeting message when called. The HTML body contains a single div element that is associated with the `myApp` module and `myCtrl` controller. Inside the div element, there is an input field and a button. The input field is bound to the scope variable `name` using the `ng-model` directive. The button is associated with the `greeting` function using the `ng-click` directive.

Parts of the example:

1. `<script>` tag to include the AngularJS library.
2. `var app = angular.module('myApp', []);` to create the AngularJS module.
3. `app.controller('myCtrl', function($scope) {` to create the controller with a single scope variable `name`.
4. `$scope.greeting = function() {` to create a function to display a greeting message.
5. `<div>` tag with `ng-app` and `ng-controller` directives to associate the module and controller with the HTML element.
6. `<input>` tag with `ng-model` directive to bind the scope variable `name` to the input field.
7. `<button>` tag with `ng-click` directive to associate the button with the `greeting` function.

## Helpful links

- [AngularJS Documentation](https://angularjs.org/)
- [AngularJS Tutorial](https://www.w3schools.com/angular/default.asp)

onelinerhub: [How do I create an example using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-create-an-example-using-angularjs)
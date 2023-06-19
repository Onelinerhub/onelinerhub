# How do I use AngularJS bindings in my code?
// plain

AngularJS bindings are a powerful feature that allow you to connect your HTML to your JavaScript code.

Here is an example of how to use AngularJS bindings in your code:

```
<div ng-app="myApp" ng-controller="myCtrl">
  <p>{{ message }}</p>
</div>

<script>
  var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope) {
    $scope.message = 'Hello World!';
  });
</script>
```

This example will output:
```Hello World!```

## Code explanation


- `<div ng-app="myApp" ng-controller="myCtrl">`: This is the HTML element that will contain the AngularJS bindings. The `ng-app` attribute defines the application name, and the `ng-controller` attribute defines the controller name.

- `<p>{{ message }}</p>`: This is the binding that will be replaced with the value of the `message` variable in the controller.

- `var app = angular.module('myApp', []);`: This is the AngularJS module that will contain the controller.

- `app.controller('myCtrl', function($scope) {`: This is the controller that will contain the `message` variable.

- `$scope.message = 'Hello World!';`: This is the value of the `message` variable.

- `});`: This is the closing bracket for the controller.

For more information on AngularJS bindings, see [the official AngularJS documentation](https://docs.angularjs.org/guide/expression).

onelinerhub: [How do I use AngularJS bindings in my code?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-bindings-in-my-code)
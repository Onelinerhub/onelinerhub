# How do I use AngularJS to create a user interface?
// plain

AngularJS is a JavaScript framework used to create web applications. It is often used to build user interfaces (UIs) for web applications. To use AngularJS to create a user interface, you need to first create an AngularJS module, which is a container for the different components of your application. You then need to create a controller, which is responsible for managing the data and logic of your application. Finally, you need to create a view, which is an HTML template that contains the UI elements and binds them to the controller.

## Example code

```
//Create an AngularJS module
var myApp = angular.module('myApp', []);

//Create a controller
myApp.controller('MyCtrl', function($scope) {
  $scope.message = 'Hello World!';
});

//Create a view
<div ng-controller="MyCtrl">
  {{message}}
</div>
```

## Output example

Hello World!

## Code explanation


1. `var myApp = angular.module('myApp', []);` - This creates an AngularJS module with the name 'myApp'.
2. `myApp.controller('MyCtrl', function($scope) {` - This creates a controller named 'MyCtrl', which is responsible for managing the data and logic of your application.
3. `$scope.message = 'Hello World!';` - This sets the value of the 'message' variable to 'Hello World!'
4. `<div ng-controller="MyCtrl">` - This binds the controller to the HTML template.
5. `{{message}}` - This displays the value of the 'message' variable.

## Helpful links
- https://angularjs.org/
- https://docs.angularjs.org/guide/module

onelinerhub: [How do I use AngularJS to create a user interface?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-create-a-user-interface)
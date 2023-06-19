# How do AngularJS and Angular versions differ?
// plain

AngularJS and Angular versions differ in several ways.

AngularJS is based on JavaScript and is an open-source framework, while Angular is based on TypeScript and is a platform.

AngularJS is an MVC (Model-View-Controller) framework, while Angular is a component-based architecture.

AngularJS is a JavaScript framework, while Angular is a platform and framework for building applications.

AngularJS uses two-way data binding, while Angular uses one-way data binding.

AngularJS is used for creating dynamic web applications, while Angular is used for creating modern web, mobile, and desktop applications.

AngularJS is a client-side framework, while Angular is a full-stack framework.

Example code for AngularJS:
```
<div ng-app="myApp" ng-controller="myCtrl">
  Name: <input type="text" ng-model="name"><br>
  You entered: {{name}}
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.name = "John Doe";
});
</script>
```

## Output example

You entered: John Doe

## Code explanation

- `<div ng-app="myApp" ng-controller="myCtrl">` - this is the AngularJS directive which defines the application and the controller.
- `Name: <input type="text" ng-model="name"><br>` - this is the input field which is bound to the "name" model.
- `You entered: {{name}}` - this is the expression which is bound to the "name" model and displays the value.
- `var app = angular.module('myApp', []);` - this is the module which defines the application.
- `app.controller('myCtrl', function($scope) {` - this is the controller which defines the scope of the application.
- `$scope.name = "John Doe";` - this is the scope variable which is set to "John Doe".

## Helpful links
- https://angular.io/
- https://docs.angularjs.org/guide/introduction

onelinerhub: [How do AngularJS and Angular versions differ?](https://onelinerhub.com/angularjs/how-do-angularjs-and-angular-versions-differ)
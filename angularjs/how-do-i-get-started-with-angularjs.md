# How do I get started with AngularJS?
// plain

Getting started with AngularJS is easy. Here are the steps to get started:

1. Include the AngularJS library in your HTML page.

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
```

2. Add the ng-app directive to the root HTML element of your application. This will tell AngularJS that the HTML element and its children constitute an AngularJS application.

```html
<html ng-app>
```

3. Add the ng-model directive to the HTML elements you want to bind to a property on the $scope object.

```html
<input type="text" ng-model="name">
```

4. Add the ng-controller directive to the HTML element which will be the parent of the HTML elements you want to bind to a property on the $scope object.

```html
<div ng-controller="MyController">
```

5. Create a controller in your JavaScript code that will be responsible for initializing the $scope object.

```javascript
function MyController($scope) {
    $scope.name = '';
}
```

6. Add the controller to the ng-app module.

```javascript
var app = angular.module('myApp', []);
app.controller('MyController', MyController);
```

7. Initialize the AngularJS application using the ng-app directive.

```html
<html ng-app="myApp">
```

For more information, please refer to the [AngularJS Documentation](https://angularjs.org/).

onelinerhub: [How do I get started with AngularJS?](https://onelinerhub.com/angularjs/how-do-i-get-started-with-angularjs)
# How do I use AngularJS to create a document?
// plain

AngularJS is a JavaScript framework that can be used to create a document. To create a document using AngularJS, you need to set up an AngularJS application. This involves adding the AngularJS library to your HTML file and setting up the module, controller, and view.

```
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
</head>
<body>

<div ng-controller="myCtrl">
  <h1>{{myHeader}}</h1>
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.myHeader = "Hello World!";
});
</script>

</body>
</html>
```
This will output:

```
Hello World!
```

The code consists of the following parts:

1. The HTML file which includes the AngularJS library:
```
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
```
2. The div which sets up the module, controller, and view:
```
<div ng-controller="myCtrl">
```
3. The controller which sets up the scope:
```
app.controller('myCtrl', function($scope) {
    $scope.myHeader = "Hello World!";
});
```
4. The view which displays the scope:
```
<h1>{{myHeader}}</h1>
```

For more information on creating documents using AngularJS, see the following links:

- [AngularJS Tutorial](https://www.tutorialspoint.com/angularjs/index.htm)
- [AngularJS Documentation](https://docs.angularjs.org/guide/introduction)

onelinerhub: [How do I use AngularJS to create a document?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-create-a-document)
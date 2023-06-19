# course

How can I find an online course for learning AngularJS?
// plain

A great online course for learning AngularJS is [Egghead.io](https://egghead.io/courses/angularjs-applications-from-scratch). This course covers the fundamentals of AngularJS, from setting up an application to building a complete single-page application. It includes video lessons, code examples, and interactive exercises.

For example, the course covers how to create an app with a controller and a view. The following code block shows how to create a controller and assign it to an app:

```
var app = angular.module('myApp', []);

app.controller('myController', function($scope) {
  $scope.message = 'Hello World';
});
```

In this code block, `app` is the name of the app and `myController` is the name of the controller. The controller contains a `$scope` object, which is used to share data between the controller and the view. The `$scope.message` property is set to `'Hello World'`.

The course also covers how to create views with HTML and data bindings. The following code block shows how to use the `ng-controller` directive to bind the controller to the view:

```
<div ng-controller="myController">
  {{ message }}
</div>
```

In this code block, the `ng-controller` directive is used to bind the `myController` controller to the view. The `{{message}}` expression is used to display the value of the `$scope.message` property.

The course also covers more advanced topics such as services, directives, and filters. It is a great course for anyone looking to learn the fundamentals of AngularJS.

onelinerhub: [course

How can I find an online course for learning AngularJS?](https://onelinerhub.com/angularjs/course--how-can-i-find-an-online-course-for-learning-angularjs)
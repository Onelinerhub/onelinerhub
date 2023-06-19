# How can I use AngularJS to bind HTML elements?
// plain

AngularJS provides two-way data binding, which allows HTML elements to be bound to data models. This means that when the data model changes, the HTML elements automatically update to reflect the changes.

For example, the following code block uses AngularJS to bind an HTML element to a data model:

```
<div ng-app="myApp" ng-controller="myCtrl">
  <p>{{message}}</p>
</div>

<script>
  angular.module('myApp', []).controller('myCtrl', function($scope) {
    $scope.message = "Hello World!";
  });
</script>
```

The output of the above code will be:

```
Hello World!
```

The code has the following parts:

1. The `<div>` element with the `ng-app` and `ng-controller` attributes. This tells AngularJS to create an application and a controller.

2. The `{{message}}` expression inside the `<p>` element. This is the data binding expression which tells AngularJS to bind the data model to the HTML element.

3. The `angular.module()` and `.controller()` methods. These methods are used to define the application and the controller.

4. The `$scope.message` variable. This is the data model which is bound to the HTML element.

For more information on using AngularJS to bind HTML elements, see the [AngularJS Documentation](https://docs.angularjs.org/guide/databinding).

onelinerhub: [How can I use AngularJS to bind HTML elements?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-bind-html-elements)
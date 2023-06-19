# How do I use an AngularJS module?
// plain

An AngularJS module is a container for the different components of an AngularJS app. It helps to organize and maintain code by keeping related code together.

To use an AngularJS module, you must first define it with the `angular.module()` function. This function takes two parameters: the name of the module and an array of other modules that the module depends on.

```javascript
var myApp = angular.module('myApp', []);
```

The code above defines a module named `myApp` that does not depend on any other modules.

Next, you can add various components to your module, such as controllers, directives, filters, and services. For example, to add a controller to `myApp`, you would use the `.controller()` method:

```javascript
myApp.controller('myController', function($scope) {
  $scope.message = 'Hello World!';
});
```

The code above defines a controller named `myController` that sets the `message` variable to `Hello World!`.

Finally, you can use the module in your HTML by adding the `ng-app` directive to the `<html>` tag:

```html
<html ng-app="myApp">
  ...
</html>
```

The code above tells AngularJS to use the `myApp` module for the entire page.

For more information on AngularJS modules, see the [AngularJS documentation](https://docs.angularjs.org/guide/module).

onelinerhub: [How do I use an AngularJS module?](https://onelinerhub.com/angularjs/how-do-i-use-an-angularjs-module)
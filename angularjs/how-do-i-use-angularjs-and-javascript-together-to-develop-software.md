# How do I use AngularJS and JavaScript together to develop software?
// plain

AngularJS is a JavaScript-based open-source front-end web application framework mainly maintained by Google and by a community of individuals and corporations to address many of the challenges encountered in developing single-page applications. It aims to simplify both the development and the testing of such applications by providing a framework for client-side model–view–controller (MVC) and model–view–viewmodel (MVVM) architectures, along with components commonly used in rich Internet applications.

JavaScript is a high-level, interpreted programming language that conforms to the ECMAScript specification. It is a language that is also characterized as dynamic, weakly typed, prototype-based and multi-paradigm.

AngularJS and JavaScript can be used together to develop software. For example, the following code block uses AngularJS directives to render a simple HTML page with a button that, when clicked, will display a message using JavaScript:

```
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>
  </head>
  <body>
    <div ng-app="myApp" ng-controller="myCtrl">
      <button ng-click="myFunc()">Click me!</button>
      <p>{{message}}</p>
    </div>
    <script>
      var app = angular.module('myApp', []);
      app.controller('myCtrl', function($scope) {
        $scope.message = "";
        $scope.myFunc = function() {
          $scope.message = "Hello World!";
        }
      });
    </script>
  </body>
</html>
```

## Output example


When the button is clicked, the message "Hello World!" is displayed.

The code block consists of the following parts:

1. The `<script>` tag with the `src` attribute pointing to the AngularJS library. This is used to include the AngularJS library in the HTML page.

2. The `<div>` tag with the `ng-app` and `ng-controller` attributes. This is used to define the scope of the AngularJS application and the controller function.

3. The `<button>` tag with the `ng-click` attribute. This is used to bind a click event to the button, which will call the `myFunc()` function when clicked.

4. The `<p>` tag with the `{{message}}` expression. This is used to display the value of the `message` variable.

5. The `<script>` tag containing the `myApp` module and `myCtrl` controller function. The `myFunc()` function is defined inside the controller function, and it is used to set the value of the `message` variable when the button is clicked.

## Helpful links

- [AngularJS](https://angularjs.org/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

onelinerhub: [How do I use AngularJS and JavaScript together to develop software?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-and-javascript-together-to-develop-software)
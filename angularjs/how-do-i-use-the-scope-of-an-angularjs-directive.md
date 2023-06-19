# How do I use the scope of an AngularJS directive?
// plain

Using the scope of an AngularJS directive allows you to pass data and functions into the directive.

For example, the following code block is a directive that uses the scope to pass in a message:
```
angular.module('myApp', [])
  .directive('myDirective', function() {
    return {
      scope: {
        message: '@'
      },
      template: '<div>{{message}}</div>'
    }
  });
```

The `scope` property in the directive sets the scope of the directive. In this case, it is set to accept a message. The `@` symbol is used to bind the message to the directive's scope.

The template then uses the message passed in to the directive to display the message.

To use the directive, we can then bind the message to the directive:
```
<my-directive message="Hello World!"></my-directive>
```

This will then render the message `Hello World!` to the page.

The scope of a directive can also be used to pass in functions. For example, the following code block is a directive that uses the scope to pass in a function:
```
angular.module('myApp', [])
  .directive('myDirective', function() {
    return {
      scope: {
        action: '&'
      },
      template: '<div ng-click="action()">Click me!</div>'
    }
  });
```

The `scope` property in the directive sets the scope of the directive. In this case, it is set to accept a function. The `&` symbol is used to bind the function to the directive's scope.

The template then uses the function passed in to the directive to execute the function when the element is clicked.

To use the directive, we can then bind the function to the directive:
```
<my-directive action="myFunction()"></my-directive>
```

This will then execute the function `myFunction()` when the element is clicked.

**## Helpful links**
- [AngularJS Directive Documentation](https://docs.angularjs.org/guide/directive)

onelinerhub: [How do I use the scope of an AngularJS directive?](https://onelinerhub.com/angularjs/how-do-i-use-the-scope-of-an-angularjs-directive)
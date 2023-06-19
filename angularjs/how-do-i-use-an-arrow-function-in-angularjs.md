# How do I use an arrow function in AngularJS?
// plain

An arrow function is a type of JavaScript function that uses the `=>` syntax to define the function. In AngularJS, arrow functions can be used to create custom filters, directives, and services.

For example, to create a custom filter to capitalize the first letter of a string, the following code can be used:

```
angular.module('myApp', [])
  .filter('capitalize', () => {
    return (input) => {
      return input.charAt(0).toUpperCase() + input.slice(1);
    }
  });
```

This code will create a `capitalize` filter that can be used in the HTML template as follows:

```
<p>{{ 'hello world' | capitalize }}</p>
```

The output of this code will be:

```
Hello world
```

The code consists of the following parts:

- `angular.module('myApp', [])` - this sets up the module for the filter
- `.filter('capitalize', () => {})` - this defines the `capitalize` filter
- `return (input) => {...}` - this defines the function that will be used for the filter
- `input.charAt(0).toUpperCase() + input.slice(1)` - this is the actual logic of the filter, which takes the first character of the input string and capitalizes it, then adds the rest of the string

For more information on arrow functions in AngularJS, see the following links:

- [AngularJS Documentation on Filters](https://docs.angularjs.org/guide/filter)
- [MDN Web Docs on Arrow Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)

onelinerhub: [How do I use an arrow function in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-use-an-arrow-function-in-angularjs)
# How can I use angular.element in an AngularJS application?
// plain

Angular.element is a global function used to wrap a raw DOM element or HTML string as a jQuery element. It can be used to access DOM elements, manipulate DOM elements, and bind event handlers.

## Example code

```
var element = angular.element('<div>Hello World</div>');
console.log(element);
```

## Output example

```
[<div>​Hello World​</div>​]
```

The code above wraps a HTML string as jQuery element and logs it in the console.

## Code explanation


- `angular.element()` - wraps a raw DOM element or HTML string as a jQuery element
- `'<div>Hello World</div>'` - the HTML string that is wrapped as a jQuery element
- `console.log(element)` - logs the jQuery element in the console

## Helpful links
- [AngularJS API Reference - angular.element](https://docs.angularjs.org/api/ng/function/angular.element)
- [jQuery API Documentation](https://api.jquery.com/)

onelinerhub: [How can I use angular.element in an AngularJS application?](https://onelinerhub.com/angularjs/how-can-i-use-angular-element-in-an-angularjs-application)
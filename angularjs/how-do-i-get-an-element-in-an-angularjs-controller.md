# How do I get an element in an AngularJS controller?
// plain

To get an element in an AngularJS controller, you can use the `angular.element` method. This method takes a selector and an optional context element as arguments and returns the element.

For example, the following code will select the element with the id `myElement` and store it in the `myElement` variable:
```
var myElement = angular.element('#myElement');
```

The parts of the code are:
- `angular.element`: The method that takes a selector and an optional context element as arguments and returns the element.
- `'#myElement'`: The selector that is used to select the element with the id `myElement`.
- `var myElement`: The variable that stores the element.

## Helpful links
- [angular.element() - AngularJS](https://docs.angularjs.org/api/ng/function/angular.element)

onelinerhub: [How do I get an element in an AngularJS controller?](https://onelinerhub.com/angularjs/how-do-i-get-an-element-in-an-angularjs-controller)
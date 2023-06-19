# How can I use AngularJS JQLite to manipulate the DOM?
// plain

JQLite is a subset of jQuery that is included in AngularJS and provides limited DOM manipulation functions for AngularJS applications. It can be used to perform basic DOM manipulation tasks like selecting elements, adding and removing elements, and handling events.

## Example code


```
// Select element with id "myElement"
var element = angular.element(document.getElementById('myElement'));

// Add a class to the element
element.addClass('myClass');

// Remove the element
element.remove();
```

The example code selects an element with an id of `myElement`, adds a class called `myClass` and then removes the element from the DOM.

## Code explanation


- `angular.element(document.getElementById('myElement'))` - This line selects the element with the id of `myElement` using the `document.getElementById()` method and wraps it in an AngularJS element object.

- `element.addClass('myClass')` - This line adds the class `myClass` to the selected element.

- `element.remove()` - This line removes the element from the DOM.

## Helpful links

- [AngularJS JQLite Documentation](https://docs.angularjs.org/api/ng/function/angular.element)
- [jQuery Documentation](https://api.jquery.com/)

onelinerhub: [How can I use AngularJS JQLite to manipulate the DOM?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-jqlite-to-manipulate-the-dom)
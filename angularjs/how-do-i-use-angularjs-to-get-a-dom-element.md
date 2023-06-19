# How do I use AngularJS to get a DOM element?
// plain

To use AngularJS to get a DOM element, you can use the `angular.element()` function. This function takes a CSS selector and returns a wrapped element object, which can be used to access the DOM element.

For example:
```javascript
var element = angular.element('div.my-class');
```
This will return a wrapped element object that corresponds to the first `div` element with a class of `my-class`.

The following list explains the parts of the code above:
* `angular.element()` - This is the AngularJS function used to get a DOM element.
* `div.my-class` - This is the CSS selector used to select the element.

More information about `angular.element()` can be found in the [AngularJS API documentation](https://docs.angularjs.org/api/ng/function/angular.element).

onelinerhub: [How do I use AngularJS to get a DOM element?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-get-a-dom-element)
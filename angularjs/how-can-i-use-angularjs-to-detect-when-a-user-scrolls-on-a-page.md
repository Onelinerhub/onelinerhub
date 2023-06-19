# How can I use AngularJS to detect when a user scrolls on a page?
// plain

To detect when a user scrolls on a page using AngularJS, you can use the `angular.element` function to get the current scroll position of the page.

```javascript
angular.element(window).bind('scroll', function() {
  var windowScrollPosition = window.pageYOffset;
  console.log('The current scroll position is ' + windowScrollPosition);
});
```

This code will log the current scroll position of the page to the console when the user scrolls.

The code consists of the following parts:

- `angular.element(window)` - This function retrieves the current window object.
- `.bind('scroll', function()` - This binds an event listener to the window object that listens for the 'scroll' event.
- `var windowScrollPosition = window.pageYOffset` - This stores the current scroll position of the page in a variable.
- `console.log('The current scroll position is ' + windowScrollPosition)` - This logs the current scroll position to the console.

For more information, see the following links:

- [AngularJS API Reference - angular.element](https://docs.angularjs.org/api/ng/function/angular.element)
- [MDN Web API Reference - Window.pageYOffset](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageYOffset)

onelinerhub: [How can I use AngularJS to detect when a user scrolls on a page?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-detect-when-a-user-scrolls-on-a-page)
# How can I use the AngularJS keydown event to trigger a function?
// plain

To use the AngularJS keydown event to trigger a function, you need to use the [`ng-keydown`](https://docs.angularjs.org/api/ng/directive/ngKeydown) directive. This directive allows you to specify an expression to execute when a key is pressed. The expression will be evaluated within the scope of the current controller.

For example, the following code block will trigger a function named `keydownFn` when the enter key is pressed:

```html
<input type="text" ng-keydown="keydownFn($event)" />
```

The `$event` parameter is an [`$event` object](https://docs.angularjs.org/api/ng/type/$event) that contains information about the key that was pressed.

In the controller, the `keydownFn` function can be defined as follows:

```js
$scope.keydownFn = function($event) {
  if ($event.keyCode == 13) {
    // do something when the enter key is pressed
  }
}
```

The `$event.keyCode` property contains the key code of the key that was pressed. In this example, the key code 13 represents the enter key.

For more information, see the [AngularJS ng-keydown directive](https://docs.angularjs.org/api/ng/directive/ngKeydown) documentation.

onelinerhub: [How can I use the AngularJS keydown event to trigger a function?](https://onelinerhub.com/angularjs/how-can-i-use-the-angularjs-keydown-event-to-trigger-a-function)
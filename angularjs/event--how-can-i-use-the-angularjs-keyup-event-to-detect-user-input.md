# event

How can I use the AngularJS keyup event to detect user input?
// plain

The AngularJS `keyup` event is a built-in event that fires when a user presses a key on their keyboard. It can be used to detect user input in the form of keystrokes.

The following example code binds an event listener to an HTML element, and logs the key that was pressed:

```html
<div ng-app="app" ng-controller="Ctrl">
  <input type="text" ng-keyup="keyUp($event)" />
</div>

<script>
  angular.module('app', []).controller('Ctrl', function($scope) {
    $scope.keyUp = function($event) {
      console.log($event.key);
    };
  });
</script>
```

When a user presses a key, the `keyUp` function is called and the `key` property of the `$event` object is logged. For example, if the user presses the letter 'a', the output would be:

```
a
```

The code consists of the following parts:

1. The HTML element with the `ng-keyup` directive, which binds the `keyUp` function to the `keyup` event.
2. The `keyUp` function, which is called when the `keyup` event fires. It logs the `key` property of the `$event` object.

For more information, see the [AngularJS Documentation](https://docs.angularjs.org/api/ng/directive/ngKeyup).

onelinerhub: [event

How can I use the AngularJS keyup event to detect user input?](https://onelinerhub.com/angularjs/event--how-can-i-use-the-angularjs-keyup-event-to-detect-user-input)
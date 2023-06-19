# How can I use the AngularJS keydown event to detect when the Enter key is pressed?
// plain

The AngularJS keydown event can be used to detect when the Enter key is pressed. To do this, you need to use the `keydown` event and check the key code of the pressed key.

## Example code

```javascript
angular.module('myApp', [])
  .controller('MyCtrl', function($scope) {
    $scope.onKeyDown = function(event) {
      if (event.keyCode === 13) {
        alert("Enter was pressed!");
      }
    };
  });
```

## Output example
 `Alert: "Enter was pressed!"`

The code above uses the `keydown` event to detect when the Enter key is pressed. It checks the `keyCode` of the pressed key, which is 13 for Enter. If the keyCode is 13, then an alert is triggered.

The code consists of the following parts:

1. `angular.module('myApp', [])`: This creates a new module called `myApp` and sets it up for use in the application.

2. `.controller('MyCtrl', function($scope) {`: This creates a new controller called `MyCtrl` and sets up the scope of the controller.

3. `$scope.onKeyDown = function(event) {`: This creates a new function called `onKeyDown` and sets it up to be called when the `keydown` event is triggered.

4. `if (event.keyCode === 13) {`: This checks the `keyCode` of the pressed key. If the keyCode is 13, then the code inside the `if` statement will be executed.

5. `alert("Enter was pressed!");`: This triggers an alert that says "Enter was pressed!"

## Helpful links

- [AngularJS keydown event](https://docs.angularjs.org/api/ng/directive/ngKeydown)
- [Event.keyCode](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/keyCode)

onelinerhub: [How can I use the AngularJS keydown event to detect when the Enter key is pressed?](https://onelinerhub.com/angularjs/how-can-i-use-the-angularjs-keydown-event-to-detect-when-the-enter-key-is-pressed)
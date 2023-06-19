# How do I use AngularJS input events?
// plain

Using AngularJS input events allows you to bind data to HTML input fields and respond to user input events such as keystrokes, mouse clicks, and more.

For example, the following code binds the `keyup` event to an input field and logs the input value to the console:

```
<input type="text" ng-model="myInput" ng-keyup="logInput()" />

$scope.logInput = function() {
  console.log($scope.myInput);
}
```

When a user types in the input field, the `logInput()` function will be called and the input value will be logged to the console.

In addition to `keyup`, AngularJS also supports the following input events:

* `ng-keydown`
* `ng-keypress`
* `ng-change`
* `ng-focus`
* `ng-blur`
* `ng-cut`
* `ng-paste`

For more information, see the [AngularJS Input Events documentation](https://docs.angularjs.org/guide/forms#input-controls).

onelinerhub: [How do I use AngularJS input events?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-input-events)
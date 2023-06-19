# How can I use AngularJS to detect a keypress event?
// plain

To detect a keypress event using AngularJS, you can use the `ng-keydown` directive. `ng-keydown` takes an expression to evaluate upon keydown event.

For example, the following code will log the keycode of the pressed key when a key is pressed.

```html
<div ng-app="myApp" ng-controller="myCtrl">
  <input type="text" ng-keydown="keydown($event)">
</div>

<script>
  var app = angular.module('myApp', []);
  app.controller('myCtrl', function($scope) {
    $scope.keydown = function($event){
      console.log($event.keyCode);
    }
  });
</script>
```

## Output example

```
<keycode>
```

The code consists of the following parts:

1. `<div ng-app="myApp" ng-controller="myCtrl">` - This defines the scope of the AngularJS application.

2. `<input type="text" ng-keydown="keydown($event)">` - This defines the directive `ng-keydown` which takes an expression to evaluate upon keydown event. In this case, the expression is `keydown($event)`.

3. `app.controller('myCtrl', function($scope) {` - This defines the controller `myCtrl` which is used to define the scope of the application.

4. `$scope.keydown = function($event){` - This defines the function `keydown` which is used to log the keycode of the pressed key.

5. `console.log($event.keyCode);` - This logs the keycode of the pressed key.

## Helpful links
- [AngularJS Documentation - ng-keydown](https://docs.angularjs.org/api/ng/directive/ngKeydown)
- [w3schools - AngularJS ng-keydown Directive](https://www.w3schools.com/angular/ng_ng-keydown.asp)

onelinerhub: [How can I use AngularJS to detect a keypress event?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-detect-a-keypress-event)
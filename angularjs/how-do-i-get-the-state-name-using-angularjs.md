# How do I get the state name using AngularJS?
// plain

To get the state name using AngularJS, you can use the `$location` service. This service provides information about the current URL, including the current state.

```javascript
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $location) {
    $scope.stateName = $location.path();
});
```

The `$location.path()` returns the current state name as a string.

## Code explanation

* `var app = angular.module('myApp', [])`: This creates a new AngularJS module named `myApp`.
* `app.controller('myCtrl', function($scope, $location) {`: This creates a new controller called `myCtrl`, which takes `$scope` and `$location` as parameters.
* `$scope.stateName = $location.path();`: This assigns the state name to the `stateName` variable in the `$scope` object.
* `});`: This closes the `myCtrl` controller.

## Helpful links
* [AngularJS $location Service](https://docs.angularjs.org/api/ng/service/$location)
* [AngularJS Tutorial](https://www.w3schools.com/angular/angular_intro.asp)

onelinerhub: [How do I get the state name using AngularJS?](https://onelinerhub.com/angularjs/how-do-i-get-the-state-name-using-angularjs)
# How can I reload a page using AngularJS?
// plain

Reloading a page using AngularJS is possible by using the `$route.reload()` method. This method will reload the current route, causing the view to update with the current data.

## Example code

```
var app = angular.module('myApp', []);

app.controller('myCtrl', function($scope, $route) {
  $scope.reloadRoute = function() {
    $route.reload();
  }
});
```

This example code creates a controller called `myCtrl` which includes a function called `reloadRoute` which uses the `$route.reload()` method.

## Code explanation

- `var app = angular.module('myApp', []);` - This creates an AngularJS module called `myApp`
- `app.controller('myCtrl', function($scope, $route) {` - This creates a controller called `myCtrl` which includes the `$scope` and `$route` parameters
- `$scope.reloadRoute = function() {` - This creates a function called `reloadRoute` which is attached to the `$scope`
- `$route.reload();` - This calls the `$route.reload()` method which will reload the current route

## Helpful links
- [AngularJS Documentation - `$route`](https://docs.angularjs.org/api/ngRoute/service/$route)
- [AngularJS Documentation - `$route.reload()`](https://docs.angularjs.org/api/ngRoute/service/$route#reload)

onelinerhub: [How can I reload a page using AngularJS?](https://onelinerhub.com/angularjs/how-can-i-reload-a-page-using-angularjs)
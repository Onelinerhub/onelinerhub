# How do I reload a component in AngularJS?
// plain

To reload a component in AngularJS, you can use the `$route.reload()` method. This will reload the current active route, causing any associated controller to be executed again.

For example:
```
angular.module('myApp', ['ngRoute'])
  .controller('MyController', function($scope, $route) {
    $scope.reloadRoute = function() {
      $route.reload();
    }
  });
```

The above code will reload the current active route when the `reloadRoute` function is called.

The `$route.reload()` method has the following parts:
- `$route`: The AngularJS service that provides access to the current route.
- `reload()`: The method that reloads the current active route.

For more information, see the [AngularJS $route Documentation](https://docs.angularjs.org/api/ngRoute/service/$route).

onelinerhub: [How do I reload a component in AngularJS?](https://onelinerhub.com/angularjs/how-do-i-reload-a-component-in-angularjs)
# How do I use the AngularJS Location Service to update the URL?
// plain

The AngularJS Location Service is used to update the URL of a web page. It is a service that can be used to manipulate the browser's URL in various ways, such as changing the path, search, or hash.

## Example code

```
angular.module('myApp', [])
.controller('MyController', ['$scope', '$location', function($scope, $location) {
  $scope.updateUrl = function() {
    $location.url('/new-url');
  };
}]);
```

The code above creates a controller called `MyController` that has a function called `updateUrl`. This function uses the `$location` service to update the URL to `/new-url`.

The `$location` service has several methods that can be used to manipulate the URL. For example, `$location.path()` can be used to set the path, `$location.search()` can be used to set query string parameters, and `$location.hash()` can be used to set the hash fragment.

## Helpful links

- [AngularJS Location Service Documentation](https://docs.angularjs.org/api/ng/service/$location)
- [AngularJS Tutorial: Manipulating the URL with the $location service](https://www.sitepoint.com/angularjs-tutorial-manipulating-the-url-with-the-location-service/)

onelinerhub: [How do I use the AngularJS Location Service to update the URL?](https://onelinerhub.com/angularjs/how-do-i-use-the-angularjs-location-service-to-update-the-url)
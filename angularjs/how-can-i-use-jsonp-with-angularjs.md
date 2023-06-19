# How can I use JSONP with AngularJS?
// plain

JSONP is a technique to bypass the Same Origin Policy (SOP) implemented by browsers. It can be used to make cross-domain requests from the client-side using JavaScript. To use JSONP with AngularJS, you need to use the `$http` service.

## Example

```javascript
angular.module('myApp', [])
  .controller('MyCtrl', function ($scope, $http) {
    $http.jsonp('http://example.com/data?callback=JSON_CALLBACK')
      .success(function (data) {
        $scope.data = data;
      });
  });
```

This example uses the `$http` service to make a JSONP request to `http://example.com/data`. The `JSON_CALLBACK` parameter is used to specify the name of the callback function that will be used to process the response.

## Code explanation


1. `angular.module`: Used to define an AngularJS module.
2. `.controller`: Used to define a controller in the module.
3. `$http.jsonp`: Used to make a JSONP request.
4. `JSON_CALLBACK`: Used to specify the name of the callback function that will be used to process the response.

For more information on using JSONP with AngularJS, please refer to the following links:

- [AngularJS $http Service API Reference](https://docs.angularjs.org/api/ng/service/$http)
- [Using JSONP with AngularJS](https://www.codeproject.com/Articles/873295/Using-JSONP-with-AngularJS)

onelinerhub: [How can I use JSONP with AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-jsonp-with-angularjs)
# How can I use an AngularJS HTTP interceptor to modify requests?
// plain

An AngularJS HTTP interceptor can be used to modify requests. To use an interceptor, it must first be registered in the $httpProvider.interceptors array.

## Example code

```
angular
  .module('myApp')
  .config(['$httpProvider', function($httpProvider) {
    $httpProvider.interceptors.push('myInterceptor');
  }])
  .factory('myInterceptor', function() {
    return {
      request: function(config) {
        // Modify the config object before returning it
        config.headers.Authorization = 'Bearer my-token';
        return config;
      }
    };
  });
```

The interceptor can then be used to modify the request before it is sent. In the example above, the interceptor adds an Authorization header with a token.

The interceptor can also be used to modify the response before it is returned to the caller. To do this, the interceptor must have a response function.

## Example code

```
angular
  .module('myApp')
  .factory('myInterceptor', function() {
    return {
      response: function(response) {
        // Modify the response object before returning it
        response.data.modified = true;
        return response;
      }
    };
  });
```

In the example above, the interceptor adds a modified property to the response data.

## Helpful links
- [AngularJS HTTP Interceptors](https://docs.angularjs.org/api/ng/service/$http#interceptors)
- [AngularJS $httpProvider Documentation](https://docs.angularjs.org/api/ng/provider/$httpProvider)

onelinerhub: [How can I use an AngularJS HTTP interceptor to modify requests?](https://onelinerhub.com/angularjs/how-can-i-use-an-angularjs-http-interceptor-to-modify-requests)
# How can I use AngularJS interceptors to modify HTTP requests?
// plain

AngularJS interceptors are a great way to modify HTTP requests. They allow you to modify the request before it’s sent, and modify the response after it’s received. Here is an example of using an interceptor to modify an HTTP request:

```
// Create the interceptor
app.factory('myHttpInterceptor', function($q) {
  return {
    // optional method
    'request': function(config) {
      // do something on success
      config.headers['X-My-Header'] = 'MyHeaderValue';
      return config;
    },

    // optional method
   'responseError': function(rejection) {
      // do something on error
      if (canRecover(rejection)) {
        return responseOrNewPromise
      }
      return $q.reject(rejection);
    }
  };
});

// Register the interceptor
app.config(function ($httpProvider) {
  $httpProvider.interceptors.push('myHttpInterceptor');
});
```

In the example above, the interceptor is created and registered with the `$httpProvider`. The `request` method is called whenever an HTTP request is made, and the `responseError` method is called whenever an error is encountered. In the `request` method, the header `X-My-Header` is added to the request with the value `MyHeaderValue`.

In summary, AngularJS interceptors can be used to modify HTTP requests. The example above shows how to add a custom header to a request.

**Code Parts Explanation**

1. `app.factory('myHttpInterceptor', function($q) {` - This line creates a new factory called `myHttpInterceptor`.
2. `'request': function(config) {` - This line creates the `request` method which is called whenever an HTTP request is made.
3. `config.headers['X-My-Header'] = 'MyHeaderValue';` - This line adds a custom header called `X-My-Header` with the value `MyHeaderValue` to the request.
4. `'responseError': function(rejection) {` - This line creates the `responseError` method which is called whenever an error is encountered.
5. `$httpProvider.interceptors.push('myHttpInterceptor');` - This line registers the interceptor with the `$httpProvider`.

**Relevant Links**

- [AngularJS Interceptors Documentation](https://docs.angularjs.org/api/ng/service/$http#interceptors)

onelinerhub: [How can I use AngularJS interceptors to modify HTTP requests?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-interceptors-to-modify-http-requests)
# post

How can I make an HTTP POST request using AngularJS?
// plain

To make an HTTP POST request using AngularJS, you can use the `$http` service. The `$http` service is a core AngularJS service that facilitates communication with the remote HTTP servers via the browser's XMLHttpRequest object or via JSONP.

## Example code

```
$http.post('/someUrl', {msg:'hello word!'}).
  success(function(data, status, headers, config) {
    // this callback will be called asynchronously
    // when the response is available
  }).
  error(function(data, status, headers, config) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
  });
```

No output is associated with this example code.

The code consists of the following parts:
- `$http.post('/someUrl', {msg:'hello word!'})`: This is the main method of the `$http` service which takes the URL of the remote server as the first parameter and an object containing the request body as the second parameter.
- `success`: This is a callback function that will be called asynchronously when the response is available.
- `error`: This is a callback function that will be called asynchronously if an error occurs or server returns response with an error status.

## Helpful links
- [AngularJS $http Service API Reference](https://docs.angularjs.org/api/ng/service/$http)
- [AngularJS $http.post() API Reference](https://docs.angularjs.org/api/ng/service/$http#post)

onelinerhub: [post

How can I make an HTTP POST request using AngularJS?](https://onelinerhub.com/angularjs/post--how-can-i-make-an-http-post-request-using-angularjs)
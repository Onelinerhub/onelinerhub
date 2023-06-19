# How do I use AngularJS to make a POST request?
// plain

Using AngularJS, you can make a POST request with the `$http` service. Here is an example:

```
$http({
  method: 'POST',
  url: '/someUrl',
  data: {myData: 'test'}
}).then(function successCallback(response) {
  // this callback will be called asynchronously
  // when the response is available
}, function errorCallback(response) {
  // called asynchronously if an error occurs
  // or server returns response with an error status.
});
```

The code consists of the following parts:

1. `$http` - the AngularJS service for making requests
2. `method` - the type of request, in this case `POST`
3. `url` - the URL for the request
4. `data` - the data to be sent in the request
5. `then` - the success and error callbacks

## Helpful links

- [AngularJS $http Service API Reference](https://docs.angularjs.org/api/ng/service/$http)

onelinerhub: [How do I use AngularJS to make a POST request?](https://onelinerhub.com/angularjs/how-do-i-use-angularjs-to-make-a-post-request)
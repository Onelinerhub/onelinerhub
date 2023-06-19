# file

How do I upload a file using AngularJS?
// plain

To upload a file using AngularJS, you can use the [`Http` service](https://docs.angularjs.org/api/ng/service/$http).

First, you need to create an `<input type="file">` element in your HTML and bind it to a variable in your controller.

```html
<input type="file" ng-model="file">
```

Then, in your controller, you can use the `Http` service to upload the file.

```js
$http.post('/upload', {file: $scope.file}).then(function(response) {
    // do something with the response
});
```

The `Http` service will send a `POST` request to the `/upload` endpoint, with the file as the request body.

The response from the server will be handled in the `then` callback. Depending on the server's response, you can do something with the response.

## Helpful links
- [AngularJS `$http` service](https://docs.angularjs.org/api/ng/service/$http)
- [AngularJS `<input type="file">`](https://docs.angularjs.org/api/ng/input/input%5Bfile%5D)

onelinerhub: [file

How do I upload a file using AngularJS?](https://onelinerhub.com/angularjs/file--how-do-i-upload-a-file-using-angularjs)
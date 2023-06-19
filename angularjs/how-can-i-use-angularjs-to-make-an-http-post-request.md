# How can I use AngularJS to make an HTTP POST request?
// plain

To use AngularJS to make an HTTP POST request, you can use the $http service. The $http service provides a method, `$http.post()`, which takes the URL, data, and configuration object as parameters. Here is an example of using $http.post() to make an HTTP POST request:

```
$http.post('/api/todos', {
    title: 'My Todo',
    description: 'My todo description'
})
.then(function(response) {
    console.log(response);
});
```

The code above will make a POST request to the `/api/todos` URL with the data `{title: 'My Todo', description: 'My todo description'}`. The response of the request will be logged to the console.

The parts of the code above are as follows:

- `$http.post()`: the method used to make an HTTP POST request
- `/api/todos`: the URL of the POST request
- `{title: 'My Todo', description: 'My todo description'}`: the data sent with the POST request
- `function(response)`: the callback function to be executed after the POST request completes
- `console.log(response)`: the code that logs the response of the POST request to the console

For more information on using $http.post() to make an HTTP POST request, see the [AngularJS documentation](https://docs.angularjs.org/api/ng/service/$http#post).

onelinerhub: [How can I use AngularJS to make an HTTP POST request?](https://onelinerhub.com/angularjs/how-can-i-use-angularjs-to-make-an-http-post-request)
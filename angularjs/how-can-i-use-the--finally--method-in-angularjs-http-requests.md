# How can I use the `finally` method in AngularJS HTTP requests?
// plain

The `finally` method is a way to execute code after an AngularJS HTTP request has been completed, regardless of whether the request was successful or not. It is a great way to handle any necessary clean-up tasks or to alert the user of the status of the request. Here is an example of how to use the `finally` method in an AngularJS HTTP request:

```javascript
$http.get('/someUrl')
  .then(function(response) {
    // handle success
  }, function(response) {
    // handle error
  })
  .finally(function() {
    console.log('Request completed!');
  });
```

## Output example
 `Request completed!`

The code above first makes an HTTP request to the specified URL. Then, it handles the response, either as a success or an error. Finally, it runs the `finally` block, which in this case logs a message to the console.

## Code explanation


- `$http.get('/someUrl')`: This is the AngularJS HTTP request.
- `.then(function(response) {...}, function(response) {...})`: This handles the response, either as success or error.
- `.finally(function() {...})`: This is the `finally` block, which runs after the response has been handled.

For more information, see the [AngularJS Documentation](https://docs.angularjs.org/api/ng/service/$http).

onelinerhub: [How can I use the `finally` method in AngularJS HTTP requests?](https://onelinerhub.com/angularjs/how-can-i-use-the--finally--method-in-angularjs-http-requests)
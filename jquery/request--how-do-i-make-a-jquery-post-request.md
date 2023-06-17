# request

How do I make a jQuery post request?
// plain

To make a jQuery post request, you can use the `$.post()` method. This method takes three parameters: the URL to make the request to, the data to send, and a callback function to execute on success. An example of a post request is shown below:

```
$.post("example.php", {name: "John", time: "2pm"},
    function(data){
        alert("Data Loaded: " + data);
    });
```

In the example above, the post request is sent to the URL `example.php` with the data `name: "John", time: "2pm"`. When the request is successful, the anonymous callback function `function(data){...}` is executed, and the response data is passed in as the `data` parameter.

The parts of the code are:

1. `$.post()`: The jQuery post method, used to make a post request.
2. `"example.php"`: The URL to make the post request to.
3. `{name: "John", time: "2pm"}`: The data to send with the post request.
4. `function(data){...}`: The callback function to execute on success.

For more information, see the [jQuery documentation](https://api.jquery.com/jquery.post/).

onelinerhub: [request

How do I make a jQuery post request?](https://onelinerhub.com/jquery/request--how-do-i-make-a-jquery-post-request)
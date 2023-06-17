# How can I use jQuery to make an asynchronous HTTP (XHR) request?
// plain

jQuery provides an easy way to make asynchronous HTTP (XHR) requests. The basic syntax for making an XHR request with jQuery is as follows:

```
$.ajax({
  url: 'http://example.com/api',
  type: 'GET',
  success: function(data) {
    // Do something with the data
  }
});
```

The code above will make an AJAX request to the specified URL using the GET method. If the request is successful, the data returned by the server will be passed to the success callback.

## Code explanation

- `url`: The URL of the request.
- `type`: The type of request, e.g. GET, POST, PUT, etc.
- `success`: A callback function that will be called if the request is successful.

## Code explanation
//api.jquery.com/jquery.ajax/).

onelinerhub: [How can I use jQuery to make an asynchronous HTTP (XHR) request?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-make-an-asynchronous-http--xhr--request)
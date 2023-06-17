# How do I use a jQuery x-csrf-token?
// plain

Using a jQuery x-csrf-token requires setting the x-csrf-token header for each AJAX request. The token can be obtained from the server and stored in a variable.

```js
// Get the x-csrf-token from the server
var csrfToken = $.get('/api/csrf-token');

// Set the x-csrf-token header for each AJAX request
$.ajaxSetup({
    headers: {
        'x-csrf-token': csrfToken
    }
});
```

To use the token, it must be set as a header in each AJAX request. The code above shows how to get the token from the server and set it as a header.

The following code shows an example of an AJAX request with the x-csrf-token header set:

```js
$.ajax({
    type: 'POST',
    url: '/api/user',
    data: { name: 'John' },
    headers: {
        'x-csrf-token': csrfToken
    },
    success: function(data) {
        console.log(data);
    }
});
```

The code above sets the x-csrf-token header in the AJAX request. This allows the server to authenticate the request and process it correctly.

## Helpful links
- [jQuery x-csrf-token](https://www.jquery-az.com/jquery-x-csrf-token/)
- [jQuery AJAX Setup](https://api.jquery.com/jquery.ajaxsetup/)

onelinerhub: [How do I use a jQuery x-csrf-token?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-x-csrf-token)
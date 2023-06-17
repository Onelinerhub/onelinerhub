# Send

How can I use jQuery's beforeSend function?
// plain

The `beforeSend` function in jQuery is a callback function that is executed before an Ajax request is sent. It allows you to modify the request before it is sent to the server. It is useful for setting custom headers, serializing data, or adding authentication information.

## Example

```javascript
$.ajax({
  type: "POST",
  url: "some.php",
  data: { name: "John", location: "Boston" },
  beforeSend: function(xhr) {
    xhr.setRequestHeader("X-Custom-Header", "MyValue");
  }
});
```

This example sends a POST request to `some.php` with a custom header `X-Custom-Header` and the value `MyValue`.

## Code explanation

- `$.ajax()`: This is the function that sends the request.
- `type`: This specifies the type of request (e.g. GET or POST).
- `url`: This is the URL of the server-side script that will receive the request.
- `data`: This is the data that will be sent in the request.
- `beforeSend`: This is the callback function that is executed before the request is sent.
- `xhr`: This is the XMLHttpRequest object that will be used to send the request.
- `setRequestHeader`: This is a function on the XMLHttpRequest object that sets a custom header.

## Helpful links
- [jQuery.ajax()](https://api.jquery.com/jquery.ajax/)
- [XMLHttpRequest.setRequestHeader()](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader)

onelinerhub: [Send

How can I use jQuery's beforeSend function?](https://onelinerhub.com/jquery/send--how-can-i-use-jquery-s-beforesend-function)
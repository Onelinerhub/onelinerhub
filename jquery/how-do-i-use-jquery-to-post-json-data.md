# How do I use jQuery to post JSON data?
// plain

jQuery can be used to post JSON data to a server using the `$.post()` method. The `$.post()` method takes three parameters: a URL, a data object, and a callback function. The URL is the URL of the server that will receive the JSON data. The data object is a JavaScript object that contains the JSON data to be sent to the server. The callback function is a function that is called after the JSON data has been posted to the server.

## Example code

```
$.post("https://example.com/api/data", {
  "name": "John Doe",
  "age": 30
}, function(data) {
  console.log(data);
});
```

Output (if any):
```
{
  "success": true
}
```

## Code explanation

- `$.post()`: This is the jQuery method used to post JSON data to a server.
- `"https://example.com/api/data"`: This is the URL of the server that will receive the JSON data.
- `{ "name": "John Doe", "age": 30 }`: This is a JavaScript object containing the JSON data to be sent to the server.
- `function(data) { console.log(data); }`: This is a callback function that is called after the JSON data has been posted to the server.

List of relevant links (if any):
- [jQuery API Documentation - $.post()](https://api.jquery.com/jquery.post/)

onelinerhub: [How do I use jQuery to post JSON data?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-post-json-data)
# How can I use d3.js to make an XMLHttpRequest?
// plain

You can use d3.js to make an XMLHttpRequest by using the `d3.xhr()` function. This function takes two arguments: the URL of the request and an optional callback function. The callback function will be called with the response object when the request is complete.

## Example code

```javascript
d3.xhr("https://jsonplaceholder.typicode.com/users/1", function(error, response) {
  if (!error && response.status === 200) {
    console.log(response.responseText);
  }
});
```

## Output example

```
{"id":1,"name":"Leanne Graham","username":"Bret","email":"Sincere@april.biz","address":{"street":"Kulas Light","suite":"Apt. 556","city":"Gwenborough","zipcode":"92998-3874","geo":{"lat":"-37.3159","lng":"81.1496"}},"phone":"1-770-736-8031 x56442","website":"hildegard.org","company":{"name":"Romaguera-Crona","catchPhrase":"Multi-layered client-server neural-net","bs":"harness real-time e-markets"}}
```

The code above has the following parts:
- `d3.xhr()`: This is the function used to make the XMLHttpRequest.
- `"https://jsonplaceholder.typicode.com/users/1"`: This is the URL of the request.
- `function(error, response)`: This is the callback function that will be called with the response object when the request is complete.
- `if (!error && response.status === 200)`: This checks to make sure there is no error and that the response status is 200 (OK).
- `console.log(response.responseText)`: This prints the response text to the console.

## Helpful links
- [d3.xhr()](https://github.com/d3/d3-request/blob/master/README.md#xhr)
- [XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)

onelinerhub: [How can I use d3.js to make an XMLHttpRequest?](https://onelinerhub.com/javascript-d3/how-can-i-use-d--js-to-make-an-xmlhttprequest)
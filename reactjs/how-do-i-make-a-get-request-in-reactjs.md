# How do I make a GET request in ReactJS?
// plain

Making a GET request in ReactJS requires the use of the `fetch` API. Fetch is an interface for fetching resources, and is available in the global scope. It returns a promise that resolves to the response of the request.

## Example code

```
fetch('https://example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
```

## Output example

```
[
  {
    name: 'John',
    age: 30
  },
  {
    name: 'Alice',
    age: 25
  }
]
```

The code above makes a GET request to the URL `https://example.com/data`. The response is then converted to JSON and logged to the console.

The code consists of three parts:
1. `fetch('https://example.com/data')` - This is the GET request, and it returns a promise.
2. `.then(response => response.json())` - This is a callback that is called when the promise is resolved. It takes the response from the request and converts it to JSON.
3. `.then(data => console.log(data))` - This is another callback that is called when the promise is resolved. It takes the JSON data and logs it to the console.

For more information, see the [MDN Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) on the Fetch API.

onelinerhub: [How do I make a GET request in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-make-a-get-request-in-reactjs)
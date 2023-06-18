# How do I make a POST request in ReactJS?
// plain

Making a POST request in ReactJS is quite easy using the `fetch` API. Here is a simple example of making a POST request with a JSON body:

```
fetch('/api/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    data: 'example',
  }),
})
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
```

The code above will make a POST request to the `/api/data` endpoint with a JSON body containing the data `example`. The response will be parsed into a JSON object and logged in the console.

The code consists of the following parts:
- `fetch`: The `fetch` API is used to make the request.
- `method`: This is set to `POST` to indicate that this is a POST request.
- `headers`: This is a set of headers that are sent with the request. In this case, the `Content-Type` header is set to `application/json` to indicate that the body of the request is JSON.
- `body`: This is the body of the request. In this case, it is a JSON object containing the data `example`.
- `then`: This is a function that is called when the response is received. In this case, the response is parsed into a JSON object and logged in the console.
- `catch`: This is a function that is called if an error occurs. In this case, the error is logged in the console.

For more information about making requests with the `fetch` API, see the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).

onelinerhub: [How do I make a POST request in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-make-a-post-request-in-reactjs)
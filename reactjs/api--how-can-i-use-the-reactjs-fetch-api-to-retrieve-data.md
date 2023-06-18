# api

How can I use the ReactJS Fetch API to retrieve data?
// plain

The ReactJS Fetch API allows you to make network requests similar to XMLHttpRequest (XHR). It provides a simple interface for fetching resources asynchronously across the network. To use the Fetch API, you need to create a new Request object and pass it as the first argument to the fetch() method.

```
let request = new Request('https://example.com/api/data', {
    method: 'GET',
    mode: 'cors',
    redirect: 'follow'
});

fetch(request)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.log(error));
```

This example code will make a GET request to the URL `https://example.com/api/data` and log the response data to the console.

## Code explanation


1. `let request = new Request('https://example.com/api/data', { ... })`: This creates a new Request object with the URL `https://example.com/api/data` and the request options.

2. `fetch(request)`: This calls the fetch() method with the Request object as the argument.

3. `.then(response => response.json())`: This is a Promise that will be called when the request is successful. It will convert the response data to a JSON object.

4. `.then(data => console.log(data))`: This is a Promise that will be called when the response data is converted to a JSON object. It will log the data to the console.

5. `.catch(error => console.log(error))`: This is a Promise that will be called if there is an error with the request. It will log the error to the console.

## Helpful links

- [MDN - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [ReactJS - Fetch Data from a REST API](https://reactjs.org/docs/faq-ajax.html#how-can-i-fetch-data-from-an-api)

onelinerhub: [api

How can I use the ReactJS Fetch API to retrieve data?](https://onelinerhub.com/reactjs/api--how-can-i-use-the-reactjs-fetch-api-to-retrieve-data)
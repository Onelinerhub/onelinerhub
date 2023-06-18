# How can I use ReactJS to create a REST API?
// plain

ReactJS can be used to create a REST API by utilizing the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) in conjunction with a [backend server](https://www.npmjs.com/package/json-server). The fetch API allows for making HTTP requests from the frontend which can be used to interact with the backend server. The backend server can be used to store and manipulate data which can be used to create a REST API.

## Example code

```
// Make a request for a user with a given ID
fetch("/users/1")
  // Parse the response as JSON
  .then(response => response.json())
  // Log the response
  .then(user => console.log(user));
```
## Output example

```
{
  id: 1,
  name: "John Doe"
}
```

The code above makes a request to the backend server for a user with an ID of 1. The response is parsed as JSON and then logged to the console. This demonstrates how the fetch API can be used to make requests to the backend server and create a REST API.

onelinerhub: [How can I use ReactJS to create a REST API?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-rest-api)
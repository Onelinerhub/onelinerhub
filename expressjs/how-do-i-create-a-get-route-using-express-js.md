# How do I create a GET route using Express.js?
// plain

To create a GET route using Express.js, you need to use the `.get()` method. This method takes two arguments: the route path, and a callback function. The callback function takes two arguments, `request` and `response`. The `request` argument is an object that contains information about the request, such as the query parameters, headers, and other data. The `response` argument is an object that allows you to send a response to the client.

Below is an example of a GET route:

```javascript
app.get('/', (request, response) => {
  response.send('Hello, World!');
});
```

The code above will send the string `Hello, World!` to the client when the `/` route is requested.

The parts of the code above are:

- `app`: This is an instance of the Express application.
- `.get()`: This is the Express method for creating a GET route.
- `/`: This is the path of the route.
- `(request, response)`: These are the arguments for the callback function.
- `response.send()`: This is a method for sending a response to the client.

## Helpful links
- [Express Documentation](https://expressjs.com/en/api.html)
- [Express Routing](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How do I create a GET route using Express.js?](https://onelinerhub.com/expressjs/how-do-i-create-a-get-route-using-express-js)
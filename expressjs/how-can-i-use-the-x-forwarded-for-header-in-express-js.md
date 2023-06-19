# How can I use the x-forwarded-for header in Express.js?
// plain

The x-forwarded-for header is a way to identify the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer. In Express.js, the x-forwarded-for header can be used to get the IP address of the client making the request.

To use the x-forwarded-for header in Express.js, you can access the header from the request object. Here is an example of how to use the x-forwarded-for header in Express.js:

```javascript
// Access the x-forwarded-for header from the request object
const xForwardedFor = req.headers['x-forwarded-for']

// Log the IP address to the console
console.log(xForwardedFor)
```

## Output example
 `192.168.1.1`

This example code accesses the x-forwarded-for header from the request object and logs the IP address to the console.

## Code explanation


- `req.headers['x-forwarded-for']`: This is used to access the x-forwarded-for header from the request object.
- `console.log(xForwardedFor)`: This is used to log the IP address to the console.

## Helpful links

- [Express.js Request Object](https://expressjs.com/en/api.html#req)
- [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

onelinerhub: [How can I use the x-forwarded-for header in Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-the-x-forwarded-for-header-in-express-js)
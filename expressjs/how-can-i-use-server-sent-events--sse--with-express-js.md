# How can I use Server-Sent Events (SSE) with Express.js?
// plain

Server-Sent Events (SSE) is a web technology that allows a web server to push data to a client (browser). It can be used with Express.js to create real-time applications.

To use SSE with Express.js, you need to install the express-sse package.

```
npm install express-sse
```

Then you need to create a new Express.js application and add the express-sse package to it.

```
const express = require('express');
const sse = require('express-sse');

const app = express();

// Create an instance of the SSE middleware
const sseMiddleware = new sse();

// Add the middleware to the Express.js app
app.use(sseMiddleware);
```

You can then use the `sseMiddleware.send()` method to send data to the client.

```
// Send data to the client
sseMiddleware.send({
  message: 'Hello from the server!'
});
```

The client can then listen for the data using the `EventSource` API.

```
// Create an EventSource
const eventSource = new EventSource('/sse');

// Listen for data
eventSource.onmessage = (event) => {
  console.log(event.data); // Outputs 'Hello from the server!'
};
```

## Helpful links

- [Express.js](https://expressjs.com/)
- [express-sse](https://www.npmjs.com/package/express-sse)
- [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

onelinerhub: [How can I use Server-Sent Events (SSE) with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-server-sent-events--sse--with-express-js)
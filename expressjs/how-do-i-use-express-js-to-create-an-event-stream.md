# How do I use Express.js to create an event stream?
// plain

Express.js is a web application framework for Node.js. It can be used to create an event stream. The following example demonstrates how to do this:

```
const express = require('express');
const app = express();

// Create an event emitter
const events = require('events');
const eventEmitter = new events.EventEmitter();

// Create an event handler
const eventHandler = () => {
  console.log('Event Fired!');
};

// Assign the event handler to an event
eventEmitter.on('eventFired', eventHandler);

// Create a route
app.get('/', (req, res) => {
  // Fire the event
  eventEmitter.emit('eventFired');
  res.send('Event Fired!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```
## Output example

```
Server started on port 3000
Event Fired!
```

The code above creates an event stream using Express.js. It begins by requiring express and creating an instance of the express application. An event emitter is then created using the events module. An event handler is then created to handle the event. The event handler is then assigned to the event emitter. A route is then created that will fire the event and send a response. Finally, the server is started.

Parts of Code Explained:

- `const express = require('express');`: This line requires the express module.
- `const app = express();`: This line creates an instance of the express application.
- `const events = require('events');`: This line requires the events module.
- `const eventEmitter = new events.EventEmitter();`: This line creates an event emitter.
- `const eventHandler = () => { console.log('Event Fired!'); };`: This line creates an event handler.
- `eventEmitter.on('eventFired', eventHandler);`: This line assigns the event handler to the event emitter.
- `app.get('/', (req, res) => { eventEmitter.emit('eventFired'); res.send('Event Fired!'); });`: This line creates a route that will fire the event and send a response.
- `app.listen(3000, () => { console.log('Server started on port 3000'); });`: This line starts the server on port 3000.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Node.js Events Documentation](https://nodejs.org/api/events.html)

onelinerhub: [How do I use Express.js to create an event stream?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-create-an-event-stream)
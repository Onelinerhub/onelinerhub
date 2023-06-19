# How do I use Express.js to create a cluster?
// plain

Express.js is a web framework for Node.js. It can be used to create a cluster of multiple processes that can run on multiple CPU cores. To create a cluster with Express.js, the [`cluster`](https://nodejs.org/api/cluster.html) module must be used. Here is an example of how to create a cluster with Express.js:

```javascript
const cluster = require('cluster');
const numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  console.log('Master process is running');

  // Fork workers
  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on('exit', (worker, code, signal) => {
    console.log(`Worker ${worker.process.pid} died`);
  });
} else {
  // Workers can share any TCP connection
  // In this case it is an HTTP server
  const express = require('express');
  const app = express();

  app.get('/', (req, res) => {
    res.send('Hello from Worker ' + cluster.worker.id);
  });

  app.listen(8000);
  console.log(`Worker ${cluster.worker.id} is running`);
}
```

This example will create a cluster of `numCPUs` workers and run an Express.js server on each one. The server will respond to requests with the message `Hello from Worker <worker id>`.

## Code explanation


1. `const cluster = require('cluster');` - This imports the `cluster` module from Node.js.
2. `const numCPUs = require('os').cpus().length;` - This gets the number of CPUs available on the system.
3. `if (cluster.isMaster) {...} else {...}` - This checks if the process is the master process. If so, it will fork workers. Otherwise, it will run the Express.js server.
4. `cluster.fork()` - This is used to fork a worker process.
5. `const express = require('express');` - This imports the Express.js module.
6. `const app = express();` - This creates an Express.js app.
7. `app.get('/', (req, res) => {...});` - This sets up a route that will respond to requests with the message `Hello from Worker <worker id>`.
8. `app.listen(8000);` - This starts the Express.js server on port `8000`.

For more information on how to use Express.js to create a cluster, please refer to the following links:

- [Express.js Clustering](https://expressjs.com/en/advanced/clustering.html)
- [Node.js Cluster Documentation](https://nodejs.org/api/cluster.html)

onelinerhub: [How do I use Express.js to create a cluster?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-create-a-cluster)
# What are the best alternatives to Express.js for web development in 2023?
// plain

In 2023, there are several alternatives to Express.js for web development. These include:

1. Koa.js: Koa.js is a lightweight web framework created by the team behind Express.js. It is written in modern JavaScript and provides a more robust set of features than Express.js. It is also more modular, allowing developers to pick and choose which features they need for their projects.

## Example code


```
const Koa = require('koa');
const app = new Koa();

app.use(async ctx => {
  ctx.body = 'Hello World';
});

app.listen(3000);
```

2. Hapi.js: Hapi.js is another popular web framework that is used for building applications and services. It is written in Node.js and provides a robust set of features for web development. It is also highly extensible and can be used to create custom plugins and modules.

## Example code


```
const Hapi = require('hapi');
const server = Hapi.server({
  port: 3000,
  host: 'localhost'
});

server.route({
  method: 'GET',
  path: '/',
  handler: (request, h) => {
    return 'Hello World';
  }
});

server.start();
```

3. Fastify: Fastify is a fast and low overhead web framework for Node.js. It is written in TypeScript and provides a robust set of features for web development. It is also highly extensible and can be used to create custom plugins and modules.

## Example code


```
const fastify = require('fastify')();

fastify.get('/', (request, reply) => {
  reply.send({ hello: 'world' });
});

fastify.listen(3000, (err, address) => {
  if (err) {
    fastify.log.error(err);
    process.exit(1);
  }
  fastify.log.info(`server listening on ${address}`);
});
```

## Output example


```
server listening on http://127.0.0.1:3000
```

These are just a few of the alternatives to Express.js for web development in 2023. For more information, please see the following links:

- [Koa.js](https://koajs.com/)
- [Hapi.js](https://hapi.dev/)
- [Fastify](https://www.fastify.io/)

onelinerhub: [What are the best alternatives to Express.js for web development in 2023?](https://onelinerhub.com/expressjs/what-are-the-best-alternatives-to-express-js-for-web-development-in-----)
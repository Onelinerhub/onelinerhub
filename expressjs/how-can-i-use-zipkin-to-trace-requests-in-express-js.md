# How can I use Zipkin to trace requests in Express.js?
// plain

Zipkin is a distributed tracing system that allows us to trace requests across multiple services. It can be used to trace requests in Express.js by using the [zipkin-instrumentation-express](https://github.com/openzipkin/zipkin-js/tree/master/packages/zipkin-instrumentation-express) package.

To use Zipkin with Express.js, first install the package:
```
npm install zipkin-instrumentation-express
```

Then, add the following code to your Express.js app:
```
const {Tracer, ExplicitContext, BatchRecorder, jsonEncoder: {JSON_V2}} = require('zipkin');
const zipkinMiddleware = require('zipkin-instrumentation-express').expressMiddleware;

const ctxImpl = new ExplicitContext();
const recorder = new BatchRecorder({
  logger: new consoleLogger()
});
const tracer = new Tracer({ctxImpl, recorder, localServiceName: 'service-name'});

const app = express();
app.use(zipkinMiddleware({tracer}));
```

This will add the Zipkin middleware to the Express.js app, which will trace requests sent to the app.

The code above includes the following parts:

1. `const {Tracer, ExplicitContext, BatchRecorder, jsonEncoder: {JSON_V2}} = require('zipkin');` - imports the necessary components from the zipkin package.
2. `const zipkinMiddleware = require('zipkin-instrumentation-express').expressMiddleware;` - imports the expressMiddleware from the zipkin-instrumentation-express package.
3. `const ctxImpl = new ExplicitContext();` - creates a new ExplicitContext instance.
4. `const recorder = new BatchRecorder({logger: new consoleLogger()});` - creates a new BatchRecorder instance.
5. `const tracer = new Tracer({ctxImpl, recorder, localServiceName: 'service-name'});` - creates a new Tracer instance.
6. `app.use(zipkinMiddleware({tracer}));` - adds the Zipkin middleware to the Express.js app.

## Helpful links
- [Zipkin](https://zipkin.io/)
- [zipkin-instrumentation-express](https://github.com/openzipkin/zipkin-js/tree/master/packages/zipkin-instrumentation-express)

onelinerhub: [How can I use Zipkin to trace requests in Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-zipkin-to-trace-requests-in-express-js)
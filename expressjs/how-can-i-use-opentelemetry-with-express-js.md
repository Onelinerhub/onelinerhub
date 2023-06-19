# How can I use OpenTelemetry with Express.js?
// plain

OpenTelemetry can be used with Express.js to instrument your application and collect telemetry data. To use OpenTelemetry with Express.js, you will need to install the `@opentelemetry/express` package and configure it.

The following example shows how to configure OpenTelemetry with Express.js:

```javascript
const express = require('express');
const { ExpressInstrumentation } = require('@opentelemetry/express');
const { NodeTracerProvider } = require('@opentelemetry/node');

const provider = new NodeTracerProvider();
provider.register();

const app = express();
const instrumentation = new ExpressInstrumentation();

instrumentation.enable(app);

// Your Express routes

app.listen(3000);
```

This example will configure OpenTelemetry with Express.js and enable instrumentation.

## Code explanation


1. `const express = require('express')`: This imports the Express.js library.
2. `const { ExpressInstrumentation } = require('@opentelemetry/express')`: This imports the OpenTelemetry Express.js instrumentation library.
3. `const { NodeTracerProvider } = require('@opentelemetry/node')`: This imports the OpenTelemetry Node.js tracer provider.
4. `provider.register()`: This registers the tracer provider with OpenTelemetry.
5. `const instrumentation = new ExpressInstrumentation()`: This creates a new OpenTelemetry Express.js instrumentation instance.
6. `instrumentation.enable(app)`: This enables instrumentation on the Express.js application.

For more information, please refer to the [OpenTelemetry Express.js documentation](https://github.com/open-telemetry/opentelemetry-js/tree/master/packages/opentelemetry-express).

onelinerhub: [How can I use OpenTelemetry with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-opentelemetry-with-express-js)
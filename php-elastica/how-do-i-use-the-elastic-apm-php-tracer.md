# How do I use the Elastic APM PHP tracer?
// plain

The Elastic APM PHP tracer can be used to monitor and debug the performance of PHP applications.

To use it, you need to install the Elastic APM PHP agent. You can do this by running the following command:
```
composer require elastic/apm-php-agent
```

Once the agent is installed, you need to configure it by setting the following environment variables:

- `ELASTIC_APM_SERVER_URL`: The URL of the Elastic APM server.
- `ELASTIC_APM_APPLICATION_NAME`: The name of the application being monitored.
- `ELASTIC_APM_ENVIRONMENT`: The environment in which the application is running (e.g. production, staging, etc.).

Once the configuration is complete, you can start tracing your application by adding the following code to the entry point of your application:
```
<?php

require_once 'vendor/autoload.php';

$agent = new \Elastic\Apm\Agent();
$agent->start();

// Your code goes here

$agent->stop();
```

This will start the tracer and trace all the requests made to the application. You can also add custom spans to trace specific parts of the application. For example:
```
<?php

$span = $agent->startSpan('my_span');

// Your code goes here

$span->end();
```

This will trace the execution of the code within the `my_span` span.

## Helpful links
- [Elastic APM PHP Agent documentation](https://www.elastic.co/guide/en/apm/agent/php/current/index.html)
- [Elastic APM PHP Agent GitHub repository](https://github.com/elastic/apm-agent-php)

onelinerhub: [How do I use the Elastic APM PHP tracer?](https://onelinerhub.com/php-elastica/how-do-i-use-the-elastic-apm-php-tracer)
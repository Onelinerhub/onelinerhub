# How can I use PHP in AWS Lambda?
// plain

PHP can be used in AWS Lambda by creating a custom runtime. The custom runtime must be a Linux executable that is responsible for bootstrapping the language runtime and processing the Lambda event payload.

The following code example shows how to create a custom runtime in PHP:

```php
<?php

// Bootstrap the language runtime
require __DIR__ . '/vendor/autoload.php';

// Process the Lambda event payload
$payload = json_decode(file_get_contents('php://input'), true);

// Handle the Lambda event
$response = handleEvent($payload);

// Return the response
echo json_encode($response);
```

The code example includes the following parts:

1. `require __DIR__ . '/vendor/autoload.php'`: This loads the Composer autoloader, which is used to include all the necessary PHP libraries.

2. `$payload = json_decode(file_get_contents('php://input'), true)`: This retrieves the Lambda event payload from the `php://input` stream.

3. `$response = handleEvent($payload)`: This calls the `handleEvent` function with the Lambda event payload as an argument.

4. `echo json_encode($response)`: This encodes the response as JSON and prints it to the output stream.

More information about custom runtimes in AWS Lambda can be found in the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html).

onelinerhub: [How can I use PHP in AWS Lambda?](https://onelinerhub.com/php-aws/how-can-i-use-php-in-aws-lambda)
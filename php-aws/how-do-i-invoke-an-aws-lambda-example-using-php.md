# How do I invoke an AWS Lambda example using PHP?
// plain

Invoking an AWS Lambda example using PHP can be done using the AWS SDK for PHP.

The following example code demonstrates how to invoke an AWS Lambda example using PHP.

```php
<?php
// Include the SDK using the Composer autoloader
require 'vendor/autoload.php';

$client = new Aws\Lambda\LambdaClient([
    'version'     => 'latest',
    'region'      => 'us-east-1',
]);

$result = $client->invoke([
    'FunctionName' => 'my-function',
    'InvocationType' => 'RequestResponse',
    'LogType' => 'Tail',
    'Payload' => 'file://payload.json',
]);

echo $result['Payload'];
```

This example code will invoke the AWS Lambda function `my-function` with the payload `file://payload.json`, and then echo the response payload.

The code consists of the following parts:

1. Requiring the AWS SDK for PHP using the Composer autoloader
2. Instantiating an AWS Lambda client using the `Aws\Lambda\LambdaClient` class
3. Invoking the `my-function` Lambda function using the `invoke()` method
4. Echoing the response payload from the Lambda function

For more information, see the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/invoking-lambda-function.html) and the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Lambda.LambdaClient.html).

onelinerhub: [How do I invoke an AWS Lambda example using PHP?](https://onelinerhub.com/php-aws/how-do-i-invoke-an-aws-lambda-example-using-php)
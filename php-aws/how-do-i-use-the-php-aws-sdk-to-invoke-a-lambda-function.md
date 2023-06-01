# How do I use the PHP AWS SDK to invoke a Lambda function?
// plain

Using the PHP AWS SDK to invoke a Lambda function is a straightforward process.

First, you'll need to install the AWS SDK using `composer`:

```
composer require aws/aws-sdk-php
```

Then, create a new `Aws\Lambda\LambdaClient` object with your AWS credentials and the desired region:

```php
$client = new Aws\Lambda\LambdaClient([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);
```

Finally, use the `invoke()` method to invoke the Lambda function. You'll need to provide the name of the function, as well as the JSON-encoded input data:

```php
$result = $client->invoke([
    'FunctionName' => 'myFunction',
    'Payload' => '{"foo":"bar"}'
]);
```

The `invoke()` method will return a `Promise` object. To get the result of the Lambda function, you can call the `get()` method:

```php
$result = $result->get();
```

The result will be a `Aws\Result` object, which contains the output and other information about the invocation.

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [AWS Lambda PHP Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Lambda.LambdaClient.html)

onelinerhub: [How do I use the PHP AWS SDK to invoke a Lambda function?](https://onelinerhub.com/php-aws/how-do-i-use-the-php-aws-sdk-to-invoke-a-lambda-function)
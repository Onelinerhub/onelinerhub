# How do I use PHP on AWS Lambda?
// plain

Using PHP on AWS Lambda is possible with the help of the Bref project. Bref is a serverless platform for PHP applications. It allows you to create and deploy PHP applications on AWS Lambda and API Gateway.

Here is an example of how to use Bref with PHP on AWS Lambda:

```php
<?php

use Bref\Context\Context;
use Bref\Event\Http\HttpEvent;

function handler(HttpEvent $event, Context $context): array
{
    return [
        'statusCode' => 200,
        'body' => 'Hello from PHP on AWS Lambda!'
    ];
}
```

This code will return a response with a status code of `200` and a body of `Hello from PHP on AWS Lambda!`.

The code consists of the following parts:

- `use Bref\Context\Context;` - This imports the `Context` class from the `Bref` package.
- `use Bref\Event\Http\HttpEvent;` - This imports the `HttpEvent` class from the `Bref` package.
- `function handler(HttpEvent $event, Context $context): array` - This is the handler function for the AWS Lambda function. It takes an `HttpEvent` and a `Context` as arguments and returns an `array`.
- `return [ ... ]` - This returns the response to the client.

For more information, please refer to the [Bref documentation](https://bref.sh/docs/).

onelinerhub: [How do I use PHP on AWS Lambda?](https://onelinerhub.com/php-aws/how-do-i-use-php-on-aws-lambda)
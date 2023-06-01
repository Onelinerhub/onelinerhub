# How can I access AWS metadata using PHP?
// plain

To access AWS metadata using PHP, you can use the [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/). The SDK provides a `getInstanceId` method that can be used to access the instance ID of the instance that the code is running on, as well as other instance metadata.

## Example code

```php
<?php

// Include the AWS SDK for PHP
require 'vendor/autoload.php';

// Create an instance of the SDK
$sdk = new Aws\Sdk([
    'version' => 'latest',
    'region'  => 'us-east-1',
]);

// Get the instance metadata
$result = $sdk->getInstanceId();

// Print out the instance ID
echo $result->get('InstanceId');

```

## Output example

```
i-0d9f8a4f6f4dcb123
```

The code above includes the following parts:

1. `require 'vendor/autoload.php'`: This line includes the AWS SDK for PHP.
2. `$sdk = new Aws\Sdk([...])`: This line creates an instance of the SDK with the specified version and region.
3. `$result = $sdk->getInstanceId()`: This line calls the `getInstanceId` method, which returns an instance of the `Aws\Result` class.
4. `echo $result->get('InstanceId')`: This line prints out the instance ID of the instance that the code is running on.

## Helpful links

- [AWS SDK for PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/)
- [getInstanceId](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-ec2-2016-11-15.html#getinstanceid)

onelinerhub: [How can I access AWS metadata using PHP?](https://onelinerhub.com/php-aws/how-can-i-access-aws-metadata-using-php)
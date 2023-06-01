# How can I use AWS Secret Manager with PHP?
// plain

AWS Secret Manager is a service that enables you to store, access, rotate, and manage secrets such as database credentials, API keys, and other secrets. It provides a secure way to store and manage secrets in an encrypted format.

You can use AWS Secret Manager with PHP by using the AWS SDK for PHP. The AWS SDK for PHP provides a set of libraries and classes that make it easy to access and interact with the AWS services, including AWS Secret Manager.

The following is an example of how to use the AWS SDK for PHP to retrieve a secret from AWS Secret Manager:

```php
<?php

// Include the AWS SDK for PHP
require 'vendor/autoload.php';

// Create the AWS SDK for PHP object
$sdk = new Aws\Sdk([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

// Create the AWS Secret Manager client
$client = $sdk->createSecretManager();

// Retrieve the secret
$result = $client->getSecretValue([
    'SecretId' => 'my-secret'
]);

// Print the secret
echo $result['SecretString'];

?>
```

The above code will output the secret stored in AWS Secret Manager with the ID `my-secret`.

The code consists of the following parts:

1. `require 'vendor/autoload.php';` - This loads the AWS SDK for PHP.
2. `$sdk = new Aws\Sdk([...])` - This creates the AWS SDK for PHP object.
3. `$client = $sdk->createSecretManager();` - This creates the AWS Secret Manager client.
4. `$result = $client->getSecretValue([...])` - This retrieves the secret.
5. `echo $result['SecretString'];` - This prints the secret.

For more information, see the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/getting-started_basic-usage.html).

onelinerhub: [How can I use AWS Secret Manager with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-aws-secret-manager-with-php)
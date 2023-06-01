# How do I use AWS Secrets Manager with PHP?
// plain

Using AWS Secrets Manager with PHP is easy. You can use the [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/) to access the Secrets Manager service.

The following example code block shows how to retrieve a secret value using the `getSecretValue` method of the `Aws\SecretsManager\SecretsManagerClient` class:

```php
<?php

use Aws\SecretsManager\SecretsManagerClient;

$client = new SecretsManagerClient([
    'region' => 'us-east-1',
    'version' => 'latest',
]);

$secretValue = $client->getSecretValue([
    'SecretId' => 'my-secret',
]);

echo $secretValue['SecretString'];
```

This code will output the secret value stored in the `my-secret` secret.

## Code explanation


1. `use Aws\SecretsManager\SecretsManagerClient;` - imports the `SecretsManagerClient` class.
2. `$client = new SecretsManagerClient([` - creates a new `SecretsManagerClient` instance.
3. `'SecretId' => 'my-secret'` - specifies the name of the secret to retrieve.
4. `$secretValue = $client->getSecretValue([` - calls the `getSecretValue` method to retrieve the secret value.
5. `echo $secretValue['SecretString'];` - outputs the secret value.

For more information, please refer to the [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html).

onelinerhub: [How do I use AWS Secrets Manager with PHP?](https://onelinerhub.com/php-aws/how-do-i-use-aws-secrets-manager-with-php)
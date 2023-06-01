# How do I use the AWS PHP SDK Secrets Manager?
// plain

The AWS PHP SDK Secrets Manager is a powerful tool for securely storing and retrieving secrets such as passwords, database connection strings, and API keys. Here's an example of how to use it:

```php
// Include the AWS SDK
require 'vendor/autoload.php';

// Instantiate the SDK
$sdk = new Aws\Sdk([
    'region' => 'us-east-1',
    'version' => 'latest'
]);

// Create a Secrets Manager client
$client = $sdk->createSecretsManager();

// Retrieve the secret
$result = $client->getSecretValue([
    'SecretId' => 'my-secret'
]);

// Print out the secret
echo $result['SecretString'];
```

The example code above will retrieve the secret stored in the `my-secret` secret and print it out.

Here is a breakdown of the code:

1. Include the AWS SDK: `require 'vendor/autoload.php';`
2. Instantiate the SDK: `$sdk = new Aws\Sdk([ 'region' => 'us-east-1', 'version' => 'latest' ]);`
3. Create a Secrets Manager client: `$client = $sdk->createSecretsManager();`
4. Retrieve the secret: `$result = $client->getSecretValue([ 'SecretId' => 'my-secret' ]);`
5. Print out the secret: `echo $result['SecretString'];`

For more information, see the [AWS PHP SDK Secrets Manager documentation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/secretsmanager.html).

onelinerhub: [How do I use the AWS PHP SDK Secrets Manager?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-php-sdk-secrets-manager)
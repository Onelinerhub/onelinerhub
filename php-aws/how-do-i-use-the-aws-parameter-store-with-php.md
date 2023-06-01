# How do I use the AWS Parameter Store with PHP?
// plain

The AWS Parameter Store is a secure and managed key-value store that can be used to store configuration data such as passwords, database connection strings, and API keys. It can be used with PHP by using the AWS SDK for PHP, which provides an API for interacting with the AWS Parameter Store.

To use the AWS Parameter Store with PHP, you first need to install the AWS SDK for PHP with Composer.

```
composer require aws/aws-sdk-php
```

Once the SDK is installed, you can create a client for the AWS Parameter Store and use the getParameters() method to retrieve the configuration data from the store.

```
<?php

require 'vendor/autoload.php';

use Aws\ParameterStore\ParameterStoreClient;

$client = new ParameterStoreClient([
    'profile' => 'default',
    'region'  => 'us-east-1',
    'version' => 'latest',
]);

$parameters = $client->getParameters([
    'Names' => ['/myapp/db/host', '/myapp/db/user', '/myapp/db/password'],
    'WithDecryption' => true,
]);

foreach ($parameters as $parameter) {
    echo $parameter['Name'] . ': ' . $parameter['Value'] . PHP_EOL;
}

```

## Output example


```
/myapp/db/host: mydatabase.example.com
/myapp/db/user: myuser
/myapp/db/password: mypassword
```

The code above does the following:

1. Loads the AWS SDK for PHP with Composer.
2. Creates a client for the AWS Parameter Store.
3. Retrieves the configuration data from the store using the getParameters() method.
4. Iterates over the parameters and prints the name and value of each parameter.

For more information, see the [AWS SDK for PHP documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/index.html) and the [AWS Parameter Store documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html).

onelinerhub: [How do I use the AWS Parameter Store with PHP?](https://onelinerhub.com/php-aws/how-do-i-use-the-aws-parameter-store-with-php)
# How can I use the PHP AWS SDK to interact with DynamoDB?
// plain

The PHP AWS SDK can be used to interact with DynamoDB. The following example code shows how to connect to a DynamoDB table and put an item into it.

```php
// Include the AWS SDK using the Composer autoloader.
require 'vendor/autoload.php';

// Create a DynamoDB client.
$sdk = new Aws\Sdk([
    'region'   => 'us-west-2',
    'version'  => 'latest'
]);
$dynamodb = $sdk->createDynamoDb();

// Create an item and put it in the table.
$response = $dynamodb->putItem([
    'TableName' => 'users',
    'Item' => [
        'username' => ['S' => 'johndoe'],
        'age' => ['N' => '27']
    ]
]);
```

The code above will create a connection to a DynamoDB table named `users`, and put an item into the table with `username` set to `johndoe` and `age` set to `27`.

The code consists of the following parts:

1. `require 'vendor/autoload.php'`: This includes the AWS SDK using the Composer autoloader.
2. `$sdk = new Aws\Sdk([...])`: This creates a new AWS SDK object with the specified configuration.
3. `$dynamodb = $sdk->createDynamoDb()`: This creates a DynamoDB client.
4. `$response = $dynamodb->putItem([...])`: This puts an item into the DynamoDB table.

For more information on using the PHP AWS SDK to interact with DynamoDB, see the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/service/dynamodb.html).

onelinerhub: [How can I use the PHP AWS SDK to interact with DynamoDB?](https://onelinerhub.com/php-aws/how-can-i-use-the-php-aws-sdk-to-interact-with-dynamodb)
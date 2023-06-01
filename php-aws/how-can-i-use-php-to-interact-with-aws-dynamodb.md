# How can I use PHP to interact with AWS DynamoDB?
// plain

PHP can be used to interact with AWS DynamoDB by using the AWS SDK for PHP. The SDK provides access to the DynamoDB API, allowing developers to easily perform operations such as creating DynamoDB tables, inserting and retrieving items, and more.

Example code for creating a table in DynamoDB using PHP:

```
<?php
require 'vendor/autoload.php';

use Aws\DynamoDb\DynamoDbClient;

$client = DynamoDbClient::factory(array(
    'region' => 'us-west-2',  // replace with your desired region
    'version' => 'latest',
));

$params = [
    'TableName' => 'my_table',
    'KeySchema' => [
        [
            'AttributeName' => 'id',
            'KeyType' => 'HASH'  //Partition key
        ]
    ],
    'AttributeDefinitions' => [
        [
            'AttributeName' => 'id',
            'AttributeType' => 'S'  //String
        ]
    ],
    'ProvisionedThroughput' => [
        'ReadCapacityUnits' => 5,
        'WriteCapacityUnits' => 6
    ]
];

try {
    $result = $client->createTable($params);
    echo "Created table.\n";

} catch (DynamoDbException $e) {
    echo "Unable to create table:\n";
    echo $e->getMessage() . "\n";
}

```

## Output example

```
Created table.
```

The code above does the following:

1. Imports the AWS SDK for PHP.
2. Creates a DynamoDB client using the provided region and version.
3. Sets up the parameters for the table to be created, including the table name, key schema, attribute definitions, and provisioned throughput.
4. Creates the table.
5. Outputs a message if the table was created successfully.

For more information on using the AWS SDK for PHP to access DynamoDB, please see the [official documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/guide/getting-started/basic-usage.html).

onelinerhub: [How can I use PHP to interact with AWS DynamoDB?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-interact-with-aws-dynamodb)
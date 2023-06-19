# How do I use Amazon DynamoDB as a key-value store?
// plain

Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. It is a key-value store that stores data as key-value pairs, where the key is a unique identifier and the value is the data associated with the key.

To use DynamoDB as a key-value store, you need to create a DynamoDB table with the key as the primary key. You can then use the AWS SDKs or the AWS CLI to perform operations on the table.

For example, to create a table in DynamoDB, you can use the following code:

```
import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Create a new table
table = dynamodb.create_table(
    TableName='my_table',
    KeySchema=[
        {
            'AttributeName': 'key',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'key',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName='my_table')

# Print out some data about the table
print(table.item_count)
```

## Output example


`0`

The code above creates a new table named `my_table` with a primary key of `key`, which is a string type. The table also has a provisioned throughput of 5 reads and 5 writes per second.

To add data to the table, you can use the `put_item` method, which takes a `Key` and `Item` parameter. The `Key` is the primary key of the item, and the `Item` is the data associated with the key.

For example, to add a new item to the table, you can use the following code:

```
import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Add an item to the table
response = dynamodb.put_item(
    TableName='my_table',
    Item={
        'key': {
            'S': 'my_key'
        },
        'data': {
            'S': 'my_data'
        }
    }
)

# Print out some data about the item
print(response['ResponseMetadata']['HTTPStatusCode'])
```

## Output example


`200`

The code above adds an item with the key `my_key` and the data `my_data` to the `my_table` table.

You can also use the `get_item` method to retrieve an item from the table. This method takes the `Key` parameter, which is the primary key of the item.

For example, to retrieve an item from the table, you can use the following code:

```
import boto3

# Create DynamoDB client
dynamodb = boto3.client('dynamodb')

# Get an item from the table
response = dynamodb.get_item(
    TableName='my_table',
    Key={
        'key': {
            'S': 'my_key'
        }
    }
)

# Print out some data about the item
print(response['Item']['data']['S'])
```

## Output example


`my_data`

The code above retrieves an item with the key `my_key` from the `my_table` table and prints out the data associated with the key.

By using the methods provided by the AWS SDKs or the AWS CLI, you can easily use Amazon DynamoDB as a key-value store.

## Helpful links

- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
- [AWS SDKs and Tools](https://aws.amazon.com/tools/)

onelinerhub: [How do I use Amazon DynamoDB as a key-value store?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-dynamodb-as-a-key-value-store)
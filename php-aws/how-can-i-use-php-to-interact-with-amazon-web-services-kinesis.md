# How can I use PHP to interact with Amazon Web Services Kinesis?
// plain

PHP can be used to interact with Amazon Web Services Kinesis by using the AWS SDK for PHP. The AWS SDK for PHP provides an API for developers to access Kinesis services from their PHP applications. Below is an example of how to put a record into a Kinesis stream using the SDK:

```php
// Create a Kinesis client using your AWS credentials
$client = new Aws\Kinesis\KinesisClient([
    'region'  => 'us-east-1',
    'version' => '2013-12-02',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

// Create a record to put in the Kinesis stream
$record = [
    'Data' => '{"message": "Hello World!"}',
    'PartitionKey' => 'partition1'
];

// Put the record in the Kinesis stream
$result = $client->putRecord([
    'StreamName' => 'my-stream',
    'Record' => $record
]);

echo "Successfully put record in Kinesis stream\n";
```

The code above creates a Kinesis client using the AWS credentials provided, creates a record to put in the Kinesis stream, and then puts the record in the Kinesis stream. The output of the code above is `Successfully put record in Kinesis stream`.

## Code explanation


1. `$client = new Aws\Kinesis\KinesisClient([ ... ])`: creates a Kinesis client using the AWS credentials provided.
2. `$record = [ ... ]`: creates a record to put in the Kinesis stream.
3. `$result = $client->putRecord([ ... ])`: puts the record in the Kinesis stream.
4. `echo "Successfully put record in Kinesis stream\n"`: outputs a message indicating that the record was successfully put in the Kinesis stream.

## Helpful links

- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [Amazon Kinesis Documentation](https://docs.aws.amazon.com/kinesis/)

onelinerhub: [How can I use PHP to interact with Amazon Web Services Kinesis?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-interact-with-amazon-web-services-kinesis)
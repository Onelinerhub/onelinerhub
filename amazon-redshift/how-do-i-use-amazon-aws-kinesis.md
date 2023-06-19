# How do I use Amazon AWS Kinesis?
// plain

Amazon AWS Kinesis is a fully-managed streaming data platform that makes it easy to collect, process, and analyze real-time streaming data at any scale. It allows you to quickly and easily create streaming applications that process data from hundreds of sources.

To use Amazon AWS Kinesis, you must first create a Kinesis stream and specify the number of shards you want for the stream. Then, you can use the Kinesis Client Library to put data into the stream and get data from the stream.

Here is an example of how to put data into a Kinesis stream using Python:

```
import boto3

# Create an Amazon Kinesis client
kinesis_client = boto3.client('kinesis')

# Put data into the stream
response = kinesis_client.put_record(
    StreamName='my-stream',
    Data=b'Hello, World!',
    PartitionKey='partitionkey1'
)

print(response)
```

The output of this example code is:
```
{
    'ShardId': 'shardId-000000000000',
    'SequenceNumber': '49591408606047363768486939004530270821842250364918832576'
}
```

This code does the following:
1. Imports the `boto3` library, which is used to interact with AWS services.
2. Creates a Kinesis client.
3. Puts the data `Hello, World!` into the stream `my-stream`, using the partition key `partitionkey1`.
4. Prints the response from the Kinesis client, which includes the shard ID and sequence number of the data that was put into the stream.

For more information, see the [Amazon Kinesis documentation](https://docs.aws.amazon.com/kinesis/index.html).

onelinerhub: [How do I use Amazon AWS Kinesis?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-aws-kinesis)
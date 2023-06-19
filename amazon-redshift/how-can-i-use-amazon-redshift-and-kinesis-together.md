# How can I use Amazon Redshift and Kinesis together?
// plain

Amazon Redshift and Kinesis can be used together to enable real-time analytics on streaming data. Redshift is a petabyte-scale data warehouse used for analytics and Kinesis is a streaming data platform.

To use Redshift and Kinesis together, you first need to set up a Kinesis Data Stream to ingest streaming data. This data can then be processed and stored in an Amazon Redshift cluster. You can use the COPY command to load streaming data into a Redshift table.

Example code to load streaming data into a Redshift table:

```SQL
COPY mytable
FROM '<Kinesis data stream ARN>'
CREDENTIALS 'aws_access_key_id=<YourAccessKeyId>;aws_secret_access_key=<YourSecretAccessKey>'
REGION 'us-east-1'
JSON '<JSON path expression>';
```

This code will copy data from the specified Kinesis data stream into the Redshift table `mytable`. The `COPY` command requires you to specify your AWS access key and secret access key in order to access the data stream. You also need to specify the region and a JSON path expression to determine which data fields should be loaded.

Once the data is loaded into Redshift, you can perform analytics on it using SQL.

## Helpful links
- [Using Amazon Redshift with Amazon Kinesis](https://docs.aws.amazon.com/redshift/latest/dg/c_using-redshift-with-kinesis.html)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [Amazon Redshift](https://aws.amazon.com/redshift/)

onelinerhub: [How can I use Amazon Redshift and Kinesis together?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-and-kinesis-together)
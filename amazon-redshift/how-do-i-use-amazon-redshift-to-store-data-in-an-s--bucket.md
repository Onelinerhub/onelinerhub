# How do I use Amazon Redshift to store data in an S3 bucket?
// plain

Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. It can be used to store data in an S3 bucket. To do this, use the `COPY` command to load data from S3 into your Redshift cluster.

## Example code

```
COPY my_table
FROM 's3://my-bucket/my-data/'
CREDENTIALS 'aws_access_key_id=<your_access_key_id>;aws_secret_access_key=<your_secret_access_key>'
CSV;
```

This command will copy data from the S3 bucket `my-bucket` into the table `my_table` in your Redshift cluster. The `CREDENTIALS` option allows you to specify your AWS access key and secret key for authentication. The `CSV` option indicates that the data is in CSV format.

## Code explanation


* `COPY` - the command to copy data from S3 into Redshift
* `my_table` - the name of the table in your Redshift cluster to copy the data into
* `s3://my-bucket/my-data/` - the S3 bucket and path to the data
* `CREDENTIALS` - option to specify your AWS access key and secret key for authentication
* `CSV` - option to indicate that the data is in CSV format

## Helpful links

* [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)
* [COPY Command Reference](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)

onelinerhub: [How do I use Amazon Redshift to store data in an S3 bucket?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-to-store-data-in-an-s--bucket)
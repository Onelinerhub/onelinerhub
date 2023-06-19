# How can I use Amazon Redshift to perform zero ETL?
// plain

Amazon Redshift can be used to perform zero ETL (Extract, Transform, Load) by leveraging its COPY command. COPY allows data to be loaded directly from Amazon S3, Amazon DynamoDB, and remote hosts, and it supports multiple data formats such as CSV, JSON, Avro, and Parquet.

## Example


```
COPY my_table
FROM 's3://my_bucket/my_data.csv'
CREDENTIALS 'aws_access_key_id=XXXXXXXXXXXXXXXXXXXX;aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
FORMAT CSV;
```

This command will copy the data from the specified S3 bucket into the table `my_table` in Redshift.

## Code explanation

1. `COPY my_table` - This is the command to copy data to a table in Redshift.
2. `FROM 's3://my_bucket/my_data.csv'` - This is the source of the data, in this case an S3 bucket.
3. `CREDENTIALS 'aws_access_key_id=XXXXXXXXXXXXXXXXXXXX;aws_secret_access_key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'` - This is the credentials used to access the S3 bucket.
4. `FORMAT CSV` - This is the data format of the source data.

## Helpful links
- [Amazon Redshift Documentation - COPY Command](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)
- [Amazon Redshift Documentation - COPY Examples](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_examples.html)

onelinerhub: [How can I use Amazon Redshift to perform zero ETL?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-to-perform-zero-etl)
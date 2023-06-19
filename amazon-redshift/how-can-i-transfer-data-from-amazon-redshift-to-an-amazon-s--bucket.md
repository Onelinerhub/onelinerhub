# How can I transfer data from Amazon Redshift to an Amazon S3 bucket?
// plain

You can transfer data from Amazon Redshift to an Amazon S3 bucket using the `COPY` command.

The following example code will copy data from a table in a Redshift cluster to an S3 bucket:
```
COPY <table_name>
FROM 's3://<bucket_name>/<data_file_path>'
CREDENTIALS 'aws_access_key_id=<access_key_id>;aws_secret_access_key=<secret_access_key>'
DELIMITER '<delimiter_character>'
IGNOREHEADER 1
```

## Code explanation

- `<table_name>`: The name of the table in the Redshift cluster.
- `<bucket_name>`: The name of the S3 bucket.
- `<data_file_path>`: The path to the data file within the S3 bucket.
- `<access_key_id>`: The AWS access key ID associated with the S3 bucket.
- `<secret_access_key>`: The AWS secret access key associated with the S3 bucket.
- `<delimiter_character>`: The delimiter character used in the data file.

For more information about the `COPY` command, please refer to the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html).

onelinerhub: [How can I transfer data from Amazon Redshift to an Amazon S3 bucket?](https://onelinerhub.com/amazon-redshift/how-can-i-transfer-data-from-amazon-redshift-to-an-amazon-s--bucket)
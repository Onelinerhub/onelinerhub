# command

How do I use the Amazon Redshift COPY command?
// plain

The Amazon Redshift COPY command is used to load data from an Amazon S3 bucket into a Redshift table. It is a very efficient way to move large amounts of data into a Redshift cluster.

To use the COPY command, you must specify the source and destination of the data, as well as the authentication credentials. Here is an example of the command:

```
COPY mytable
FROM 's3://mybucket/mydata.csv'
CREDENTIALS 'aws_access_key_id=<your_key_id>;aws_secret_access_key=<your_secret_key>'
CSV;
```

The command will copy the data from the specified S3 bucket into the table called `mytable`. The `CREDENTIALS` clause is used to provide the authentication credentials to access the S3 bucket. The `CSV` clause is used to specify that the data is in CSV format.

The COPY command also supports other data formats, such as JSON and Avro. You can find more information about the COPY command in the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html).

onelinerhub: [command

How do I use the Amazon Redshift COPY command?](https://onelinerhub.com/amazon-redshift/command--how-do-i-use-the-amazon-redshift-copy-command)
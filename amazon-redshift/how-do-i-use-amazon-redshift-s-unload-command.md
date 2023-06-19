# How do I use Amazon Redshift's UNLOAD command?
// plain

The UNLOAD command in Amazon Redshift allows you to extract data from a cluster to one or more text files on Amazon S3. This command is useful for creating backups, archiving data, or transferring data to another system for further processing.

## Example code

```
UNLOAD ('SELECT * FROM mytable')
TO 's3://mybucket/myfolder/mydata'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
```

The example code above will extract all data from the table `mytable` and store it in the S3 bucket `mybucket` in the folder `myfolder` with the file name `mydata`. The IAM role `MyRedshiftRole` is used to provide access to the S3 bucket.

## Code explanation

* `UNLOAD` - The command to initiate the unload process.
* `('SELECT * FROM mytable')` - The SELECT statement to extract the data.
* `TO 's3://mybucket/myfolder/mydata'` - The location of the S3 bucket where the data will be stored.
* `IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'` - The IAM role that provides access to the S3 bucket.

For more information on the UNLOAD command, please see the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html).

onelinerhub: [How do I use Amazon Redshift's UNLOAD command?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-s-unload-command)
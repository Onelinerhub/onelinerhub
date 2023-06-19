# How can I use Amazon Redshift Spectrum to query data stored in Amazon S3?
// plain

Amazon Redshift Spectrum is a feature of Amazon Redshift that enables users to query data stored in Amazon S3 without the need to load the data into an Amazon Redshift cluster.

To use Redshift Spectrum, you will need to create an external schema that points to the S3 bucket containing the data. Here is an example of the SQL command to create an external schema:

```SQL
CREATE EXTERNAL SCHEMA myschema
FROM DATA CATALOG
DATABASE 'mydb'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'
CREATE EXTERNAL DATABASE IF NOT EXISTS;
```

Once the external schema is created, you can query the data stored in S3 using standard SQL commands. For example, you can use the following command to query a table stored in S3:

```SQL
SELECT * FROM myschema.mytable;
```

The output of this command will be the data stored in the table in S3.

Below are the parts of the code and an explanation of what each part does:

* `CREATE EXTERNAL SCHEMA myschema` - Creates an external schema named myschema.
* `FROM DATA CATALOG DATABASE 'mydb'` - Specifies the Data Catalog database to use.
* `IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole'` - Specifies the IAM role to use.
* `CREATE EXTERNAL DATABASE IF NOT EXISTS` - Creates an external database if it does not already exist.
* `SELECT * FROM myschema.mytable;` - Queries the table stored in S3.

## Helpful links

* [Amazon Redshift Spectrum](https://aws.amazon.com/redshift/spectrum/)
* [Using Amazon Redshift Spectrum to Query Data in Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html)

onelinerhub: [How can I use Amazon Redshift Spectrum to query data stored in Amazon S3?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-spectrum-to-query-data-stored-in-amazon-s-)
# How can I use Amazon Redshift external tables?
// plain

Amazon Redshift external tables are tables that are stored outside of Amazon Redshift and are accessed using SQL commands. They allow users to query data stored in Amazon S3, Amazon DynamoDB, or any other external data source.

To use an external table, you must first create it in Amazon Redshift. This can be done using the `CREATE EXTERNAL TABLE` command. The following example creates an external table that references a CSV file stored in an Amazon S3 bucket:

```
CREATE EXTERNAL TABLE my_table (
    col1 int,
    col2 varchar(255)
)
LOCATION 's3://my-bucket/my-data.csv'
FORMAT CSV;
```

Once the external table is created, you can query it just like any other table in Amazon Redshift. For example, the following query will return all rows from the external table:

```
SELECT * FROM my_table;
```

The following list gives a more detailed explanation of the components used in the `CREATE EXTERNAL TABLE` command:

* `CREATE EXTERNAL TABLE`: This command is used to create an external table in Amazon Redshift.
* `col1 int, col2 varchar(255)`: These are the column definitions for the table.
* `LOCATION 's3://my-bucket/my-data.csv'`: This is the location of the data, in this case an Amazon S3 bucket.
* `FORMAT CSV`: This specifies the format of the data.

For more information on using external tables with Amazon Redshift, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_EXTERNAL_TABLE.html).

onelinerhub: [How can I use Amazon Redshift external tables?](https://onelinerhub.com/amazon-redshift/how-can-i-use-amazon-redshift-external-tables)
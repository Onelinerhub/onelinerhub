# How do I use Amazon Redshift to store and retrieve key-value data?
// plain

Amazon Redshift is a fully managed, petabyte-scale data warehouse service. It can be used to store and retrieve key-value data. Key-value data is stored in Amazon Redshift tables as a single column, with the key-value pairs stored as strings.

To store key-value data in Amazon Redshift, you can use the `COPY` command to load data into a table. The command requires you to specify the source of the data, the target table, and the delimiter used to separate the key-value pairs.

For example, to load the following data into a table named `my_table`:

```
key1=value1;key2=value2;key3=value3
```

You can use the following `COPY` command:

```
COPY my_table FROM 's3://my-bucket/my-file.csv'
CREDENTIALS 'aws_access_key_id=<your_access_key_id>;aws_secret_access_key=<your_secret_access_key>'
DELIMITER ';'
```

To retrieve key-value data from Amazon Redshift, you can use the `SELECT` command. For example, to retrieve the value of `key2` from the `my_table` table, you can use the following `SELECT` command:

```
SELECT split_part(column_name, '=', 2)
FROM my_table
WHERE split_part(column_name, '=', 1) = 'key2';
```

The `split_part` function is used to separate the key-value pairs, and the `WHERE` clause is used to select the desired key.

## Helpful links

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/c_loading-tables-using-COPY.html)
- [Amazon Redshift `COPY` Command Reference](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html)
- [Amazon Redshift `SELECT` Command Reference](https://docs.aws.amazon.com/redshift/latest/dg/r_SELECT_list.html)

onelinerhub: [How do I use Amazon Redshift to store and retrieve key-value data?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-to-store-and-retrieve-key-value-data)
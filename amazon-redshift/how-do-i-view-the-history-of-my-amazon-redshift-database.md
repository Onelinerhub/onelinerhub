# How do I view the history of my Amazon Redshift database?
// plain

To view the history of your Amazon Redshift database, you can use the system table `SVV_TABLE_INFO`. This table contains the history of all the tables in the database. To view the history, you must first connect to the database using the Redshift command line interface (CLI) or a third-party client.

Once connected, you can run the following SQL query:

```
SELECT
    table_name,
    create_time,
    last_altered_time
FROM
    svv_table_info;
```

This query will return a list of all the tables in the database, along with the time they were created and last altered.

The following parts are included in the example code:

* `SELECT` - This keyword tells the database that we want to retrieve data from the table.
* `table_name, create_time, last_altered_time` - These are the columns of data that we want to retrieve from the table.
* `FROM svv_table_info` - This tells the database which table we want to retrieve data from.

## Helpful links

* [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)
* [SVV_TABLE_INFO System Table](https://docs.aws.amazon.com/redshift/latest/dg/r_SVV_TABLE_INFO.html)

onelinerhub: [How do I view the history of my Amazon Redshift database?](https://onelinerhub.com/amazon-redshift/how-do-i-view-the-history-of-my-amazon-redshift-database)
# How do I use Amazon Redshift Query Editor v2.0?
// plain

Amazon Redshift Query Editor v2.0 is a web-based query editor for Amazon Redshift. It allows users to easily write, edit, and run SQL queries against Redshift databases.

To use Amazon Redshift Query Editor v2.0, open the Amazon Redshift console and select Query Editor in the navigation pane.

You can then write a query in the query editor. For example, the following query will return a list of all tables in the database:

```
SELECT *
FROM pg_catalog.pg_tables
```

The output of the query will be a list of tables in the database, including the table name, owner, schema, etc.

You can also use the query editor to execute stored procedures and other SQL commands. For example, the following command will create a new table in the database:

```
CREATE TABLE my_table (id INT, name VARCHAR(255))
```

Once you have written and executed your query, you can save it for later use.

To learn more about Amazon Redshift Query Editor v2.0, see the [documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-2.html).

onelinerhub: [How do I use Amazon Redshift Query Editor v2.0?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-query-editor-v---)
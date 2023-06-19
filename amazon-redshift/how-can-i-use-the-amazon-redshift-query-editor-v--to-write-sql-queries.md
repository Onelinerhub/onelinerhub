# How can I use the Amazon Redshift Query Editor v2 to write SQL queries?
// plain

The Amazon Redshift Query Editor v2 is a web-based query editor that allows you to write and execute SQL queries against your Amazon Redshift cluster. To use the Query Editor, you can either enter your query in the text box or upload a .sql file containing your query.

For example, the following query can be used to list all tables in the current database:
```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
```

The output of the query will be a list of all the tables in the public schema:
```
table_name
-----------
table1
table2
table3
```

## Code explanation

1. `SELECT`: used to specify which columns will be returned in the query result.
2. `FROM`: used to specify which table the columns will be retrieved from.
3. `WHERE`: used to specify the conditions that must be met for the rows to be returned.

For more information about how to use the Amazon Redshift Query Editor v2, please refer to the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor.html).

onelinerhub: [How can I use the Amazon Redshift Query Editor v2 to write SQL queries?](https://onelinerhub.com/amazon-redshift/how-can-i-use-the-amazon-redshift-query-editor-v--to-write-sql-queries)
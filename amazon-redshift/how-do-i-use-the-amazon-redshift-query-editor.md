# How do I use the Amazon Redshift Query Editor?
// plain

The Amazon Redshift Query Editor is a web-based query editor for Amazon Redshift. It provides a graphical interface for writing and executing SQL queries against your data.

To use the Amazon Redshift Query Editor, first log in to the Amazon Redshift console and select the cluster you want to query. Then select Query Editor from the navigation menu on the left.

Once the Query Editor is open, you can write and execute SQL queries against your data. For example, the following query will return the first 10 rows of the table `customers`:

```
SELECT *
FROM customers
LIMIT 10;
```

The output of this query will be the first 10 rows of the `customers` table.

The Query Editor also provides a number of other features, such as code completion, syntax highlighting, and query history. It also allows you to connect to external databases, such as PostgreSQL and MySQL.

For more information about the Amazon Redshift Query Editor, see the [documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-query-editor.html).

onelinerhub: [How do I use the Amazon Redshift Query Editor?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-query-editor)
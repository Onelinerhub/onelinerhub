# How do I use the Amazon Redshift GUI?
// plain

Using the Amazon Redshift GUI is a great way to interact with your Redshift clusters and databases. The following steps outline how to use the GUI to manage your Redshift environment:

1. Log into the AWS Management Console and select the Amazon Redshift service.
2. Select the cluster you wish to manage.
3. Click the ‘Query Editor’ button in the navigation pane.
4. Enter your SQL query in the query editor window.
5. Click the ‘Run Query’ button to execute the query.
6. The results of the query will be displayed in the query editor window.
7. You can also view the query history and view the query execution plan.

For example, the following query will list all tables in a specific Redshift database:

```
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
```

The output of this query would be a list of all the tables in the public schema.

## Helpful links

- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)
- [Using the Query Editor](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-query-editor.html)

onelinerhub: [How do I use the Amazon Redshift GUI?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-gui)
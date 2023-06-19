# How do I connect Amazon Redshift to QuickSight?
// plain

1. To connect Amazon Redshift to QuickSight, you need to create an Amazon Redshift cluster and configure the security groups to allow connections from QuickSight.

2. After creating the Redshift cluster, you will need to create a QuickSight data source. To do this, open the QuickSight console and select Manage Data from the left-hand menu.

3. Select the Redshift data source option and enter the cluster credentials.

4. Once the data source is created, you will need to create a database connection. To do this, select the Data Source Connections option from the left-hand menu.

5. Select the Redshift data source and enter the cluster credentials.

6. After creating the database connection, you can query the data from the Redshift cluster in QuickSight.

7. Here is an example of a query to retrieve data from the Redshift cluster in QuickSight:
```
SELECT * FROM table_name
```

The query will return the data from the specified table in the Redshift cluster.

## Helpful links
- [Creating a Data Source](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sources.html)
- [Creating a Database Connection](https://docs.aws.amazon.com/quicksight/latest/user/creating-database-connections.html)

onelinerhub: [How do I connect Amazon Redshift to QuickSight?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-amazon-redshift-to-quicksight-1687162529)
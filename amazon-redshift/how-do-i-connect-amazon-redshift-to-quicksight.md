# How do I connect Amazon Redshift to QuickSight?
// plain

1. To connect Amazon Redshift to QuickSight, you will need to create an Amazon Redshift cluster and an Amazon Redshift database.

2. Once the cluster and database have been created, you will need to create a data source in QuickSight. To do this, log into the QuickSight console and select "Manage Data" from the left-hand menu.

3. Select "New data source" and then select "Amazon Redshift" from the list of data sources.

4. Enter the connection details for your Amazon Redshift cluster and database, and then select "Create data source".

5. To test the connection, select "Test connection". If the connection is successful, you will see a green check mark.

6. When the connection is successful, select "Create data set" to create a data set in QuickSight.

7. Once the data set is created, you can begin to create visualizations and analyze your data.

```
Example code

// Create Amazon Redshift cluster
CREATE CLUSTER cluster_name
WITH DB_NAME = 'database_name';

// Create Amazon Redshift database
CREATE DATABASE database_name;
```

## Output example


```
CREATE CLUSTER
CREATE DATABASE
```

## Helpful links

- [QuickSight Documentation](https://docs.aws.amazon.com/quicksight/latest/user/what-is.html)
- [Creating an Amazon Redshift Cluster](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-cluster.html)
- [Creating an Amazon Redshift Database](https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html)

onelinerhub: [How do I connect Amazon Redshift to QuickSight?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-amazon-redshift-to-quicksight)
# How do I use the Amazon Redshift UI?
// plain

The Amazon Redshift UI is an easy to use graphical user interface (GUI) that allows users to create, manage, and monitor Amazon Redshift clusters. It is available through the Amazon Redshift console.

To use the Amazon Redshift UI, first log in to the Amazon Redshift console. Once logged in, you will be able to access the cluster list and create a new cluster. You can also modify existing clusters, such as adding or deleting nodes, changing cluster parameters, and setting up security groups.

When you have created your cluster, you can then use the Amazon Redshift UI to query and manage your data. You can use the query editor to write SQL statements and execute them against your cluster. You can also view query performance metrics and other cluster information.

For example, you can run the following query to get the total number of records in a table:

```
SELECT COUNT(*) FROM my_table;
```

## Output example


```
count
------
100
```

The Amazon Redshift UI also provides tools to monitor and manage your cluster such as viewing the cluster's health and performance metrics, viewing the query logs, and setting up backups.

For more information on using the Amazon Redshift UI, please refer to the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-gui.html).

onelinerhub: [How do I use the Amazon Redshift UI?](https://onelinerhub.com/amazon-redshift/how-do-i-use-the-amazon-redshift-ui)
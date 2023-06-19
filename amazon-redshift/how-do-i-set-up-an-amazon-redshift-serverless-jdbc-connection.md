# How do I set up an Amazon Redshift serverless JDBC connection?
// plain

To set up an Amazon Redshift serverless JDBC connection, first create an Amazon Redshift cluster. This can be done using the Amazon Redshift console, the AWS CLI, or an AWS SDK.

Once the cluster is created, create an Amazon Redshift JDBC URL. This URL contains the connection information for your cluster. It should look something like this:

```
jdbc:redshift://<cluster_endpoint>:<cluster_port>/<database_name>
```

Next, create a JDBC connection using the JDBC URL. This can be done using the Amazon Redshift JDBC driver. Here is an example of how to create a JDBC connection using the Amazon Redshift JDBC driver:

```
Connection conn = DriverManager.getConnection("jdbc:redshift://<cluster_endpoint>:<cluster_port>/<database_name>", "<username>", "<password>");
```

Once the connection is created, you can execute queries against your Amazon Redshift cluster.

## Code explanation

- Connection conn = DriverManager.getConnection(): Establishes a connection to the Amazon Redshift cluster.
- "jdbc:redshift://<cluster_endpoint>:<cluster_port>/<database_name>": JDBC URL containing the connection information for the cluster.
- "<username>", "<password>": Credentials used to authenticate the connection.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/getting-started.html)
- [Amazon Redshift JDBC Driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)

onelinerhub: [How do I set up an Amazon Redshift serverless JDBC connection?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-an-amazon-redshift-serverless-jdbc-connection)
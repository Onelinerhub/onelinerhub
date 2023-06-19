# How do I connect to an Amazon Redshift cluster using PostgreSQL?
// plain

To connect to an Amazon Redshift cluster using PostgreSQL, you need to have the following information:

1. The hostname of the cluster
2. The port number of the cluster
3. The database name
4. The username and password

Once you have the above information, you can use the following code to connect to the cluster:

```
import psycopg2

conn = psycopg2.connect(host="hostname",
                        port="portnumber",
                        dbname="dbname",
                        user="username",
                        password="password")
```

This will establish a connection to the cluster and return a connection object. You can then use the connection object to execute queries and other operations.

## Helpful links

1. [Connecting to an Amazon Redshift Cluster Using PostgreSQL](https://docs.aws.amazon.com/redshift/latest/dg/getting-started-connecting-to-cluster.html)
2. [psycopg2 - PostgreSQL database adapter for Python](https://pypi.org/project/psycopg2/)

onelinerhub: [How do I connect to an Amazon Redshift cluster using PostgreSQL?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-an-amazon-redshift-cluster-using-postgresql)
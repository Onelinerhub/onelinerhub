# How do I set up Amazon Redshift as a database?
// plain

1. Create a cluster in the Amazon Redshift console. This can be done by clicking the "Create Cluster" button.
2. Select a cluster type, node type, and number of nodes.
3. Configure the security settings. This includes setting up the database user and password, and setting up the security group.
4. Create the cluster.
5. Connect to the cluster. This can be done with the following example code:
```
import psycopg2

conn = psycopg2.connect(
    dbname="database_name",
    user="user_name",
    password="password",
    host="host_name",
    port="5439"
)
```
6. Create tables and load data into the tables. This can be done with SQL commands.
7. Query the data in the tables. This can also be done with SQL commands.

## Helpful links
- [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)
- [Psycopg2 Documentation](http://initd.org/psycopg/docs/)

onelinerhub: [How do I set up Amazon Redshift as a database?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-redshift-as-a-database)
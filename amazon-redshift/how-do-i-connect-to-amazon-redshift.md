# How do I connect to Amazon Redshift?
// plain

To connect to Amazon Redshift, you need to use a PostgreSQL client. You can use the `psql` command line tool, or a graphical client such as Postico.

Using the `psql` command line tool, you can connect to Amazon Redshift with the following command:
```
psql -h <hostname> -p <port> -U <username> -d <database>
```

- `hostname` is the endpoint of your cluster, which can be found in the Amazon Redshift console.
- `port` is the port your cluster is listening on, usually 5439.
- `username` is the master user of your cluster.
- `database` is the name of the database you want to connect to.

Once you have entered the command, you will be prompted to enter the password for the master user.

You can also use a graphical client such as Postico to connect to Amazon Redshift. To do this, you will need the endpoint, port, username and password for your cluster.

For more information, refer to the [Amazon Redshift documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-using-psql.html).

onelinerhub: [How do I connect to Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-amazon-redshift)
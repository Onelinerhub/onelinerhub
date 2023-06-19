# How do I log in to Amazon Redshift?
// plain

To log in to Amazon Redshift, you will need to have an AWS account and an Amazon Redshift cluster.

First, create a user with the master user credentials to access the cluster. To do this, use the following command:
```
CREATE USER username WITH PASSWORD 'password';
```

Next, grant the user access to the cluster. To do this, use the following command:
```
GRANT USAGE ON SCHEMA public TO username;
```

Once the user is created, you can log in to the cluster using the following command:
```
psql -h <cluster_endpoint> -U username -d <database_name>
```

The `<cluster_endpoint>` should be the endpoint of your Amazon Redshift cluster. The `<database_name>` should be the name of the database you want to access.

Once logged in, you can run SQL queries against the database.

For more information, see the [Amazon Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html).

onelinerhub: [How do I log in to Amazon Redshift?](https://onelinerhub.com/amazon-redshift/how-do-i-log-in-to-amazon-redshift)
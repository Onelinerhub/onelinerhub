# How can I set up Amazon RDS with PostgreSQL?
// plain

1. First, you need to create an Amazon RDS instance. To do this, log in to the [AWS Management Console](https://console.aws.amazon.com/) and navigate to the RDS dashboard.
2. On the RDS dashboard, click the ‘Create database’ button and select PostgreSQL as the engine type.
3. Next, you will need to configure the instance details such as the database instance size, storage type, and authentication method.
4. Once the instance has been created, you can access the database using the endpoint URL provided by Amazon RDS.
5. To connect to the PostgreSQL database, you will need to use a PostgreSQL client. For example, the following code uses the `psql` command line client:
```
psql "host=<endpoint> port=5432 dbname=<dbname> user=<username> password=<password>"
```
6. Once connected, you can execute SQL statements to create tables, insert data, and query the database.
7. For more information about setting up and using Amazon RDS with PostgreSQL, please see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html).

onelinerhub: [How can I set up Amazon RDS with PostgreSQL?](https://onelinerhub.com/amazon-redshift/how-can-i-set-up-amazon-rds-with-postgresql)
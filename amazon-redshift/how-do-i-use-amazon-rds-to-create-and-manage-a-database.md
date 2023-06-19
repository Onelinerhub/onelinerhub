# How do I use Amazon RDS to create and manage a database?
// plain

Amazon Relational Database Service (RDS) is a managed database service that makes it easy to set up, operate, and scale a relational database in the cloud. To create and manage a database using Amazon RDS, follow these steps:

1. Log in to the [AWS Management Console](https://console.aws.amazon.com/) and navigate to the Amazon RDS service.

2. Select the type of database you want to create. You can choose from MySQL, PostgreSQL, Oracle, Microsoft SQL Server, and Amazon Aurora.

3. Configure the details for your database. You can choose the instance type, storage, and backup options.

4. Create the database.

5. Connect to the database using an application or SQL client.

For example, to connect to a MySQL database using the MySQL command line client, you can use the following command:

```
mysql -h <hostname> -u <username> -p
```

This will prompt you for a password. Once you enter it, you will be connected to the database.

You can also use the Amazon RDS service to manage and monitor your database. This includes setting up automated backups, scaling up or down the database instance, and setting up replication for high availability.

## Helpful links

- [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Connecting to a DB Instance Running the MySQL Database Engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html)

onelinerhub: [How do I use Amazon RDS to create and manage a database?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-rds-to-create-and-manage-a-database)
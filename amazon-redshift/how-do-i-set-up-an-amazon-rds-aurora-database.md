# How do I set up an Amazon RDS Aurora database?
// plain

1. Create an Amazon RDS instance. This can be done by going to the Amazon RDS console, selecting the "Launch a DB Instance" button, and then selecting the Aurora engine.

2. Configure the instance. This includes selecting the instance class (e.g. db.t2.micro), setting the database name and master password, and selecting the database port.

3. Configure the security group. This includes setting up the security group to allow access to the instance.

4. Create a database. This can be done by running the following command in the Amazon RDS console:

```
CREATE DATABASE my_database;
```

5. Create a user. This can be done by running the following command in the Amazon RDS console:

```
CREATE USER my_user IDENTIFIED BY 'my_password';
```

6. Grant privileges to the user. This can be done by running the following command in the Amazon RDS console:

```
GRANT ALL ON my_database.* TO my_user;
```

7. Connect to the database. This can be done by using the database endpoint, username, and password to connect to the database using a database client.

## Helpful links
- [Amazon RDS Console](https://console.aws.amazon.com/rds/)
- [Connecting to an Amazon Aurora DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Connecting.html)

onelinerhub: [How do I set up an Amazon RDS Aurora database?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-an-amazon-rds-aurora-database)
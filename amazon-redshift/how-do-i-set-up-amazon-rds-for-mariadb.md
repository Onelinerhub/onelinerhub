# How do I set up Amazon RDS for MariaDB?
// plain

1. First, create an Amazon Web Services (AWS) account and log in to the AWS Management Console.
2. Select “RDS” from the “Services” menu and then select “Create Database”.
3. Select the MariaDB engine and choose the desired instance size and storage type.
4. Configure the database options, such as the database name, user name, and password.
5. Configure the network and security settings, such as the VPC, subnet group, and security group.
6. Create a database instance by clicking the “Create Database” button.
7. Once the database is created, you can connect to it using the connection string provided on the RDS console.

## Example code


```
$ mysql -h <hostname> -u <dbuser> -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 43
Server version: 10.3.22-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

## Code explanation


* `mysql` - The command to connect to the MariaDB server.
* `-h <hostname>` - The hostname of the MariaDB server.
* `-u <dbuser>` - The username of the MariaDB user.
* `-p` - Prompt for the user's password.

## Helpful links

* [Amazon RDS for MariaDB](https://aws.amazon.com/rds/mariadb/)
* [Getting Started with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/GettingStarted.RDS.html)

onelinerhub: [How do I set up Amazon RDS for MariaDB?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-for-mariadb)
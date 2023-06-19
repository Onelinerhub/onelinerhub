# How do I set up Amazon RDS for Oracle?
// plain

1. Create an Amazon Web Services (AWS) account and sign into the AWS Management Console.
2. Select the RDS service from the list of services.
3. Select the Oracle engine from the list of database engines.
4. Select the desired instance type and configure the instance.
5. Create a database instance by specifying a database name, username, and password.
6. Configure the security group to allow access to the database instance.
7. Connect to the database instance using Oracle SQL Developer.

Example code block:
```
CREATE DATABASE my_database
  USER my_user
  IDENTIFIED BY my_password;
```

## Output example

```
Database created.
```

## Code explanation

- CREATE DATABASE: creates a database with the given name
- USER: creates a user with the given username
- IDENTIFIED BY: specifies the user's password

## Helpful links
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html

onelinerhub: [How do I set up Amazon RDS for Oracle?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-for-oracle)
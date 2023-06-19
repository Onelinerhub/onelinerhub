# How do I connect to Amazon RDS?
// plain

1. First, create an Amazon Web Services (AWS) account. You can do this by going to [aws.amazon.com](https://aws.amazon.com/).
2. Next, create an Amazon Relational Database Service (RDS) instance. You can do this by going to the AWS Management Console and navigating to the RDS dashboard.
3. Once your instance is created, you can connect to it using a standard MySQL client. For example, you can use the following code to connect to your RDS instance:

```
mysql -h <endpoint> -u <username> -p
```

4. When prompted, enter the password associated with your RDS instance.
5. After entering the password, you should be connected to your RDS instance and be able to run queries.
6. You can also connect to your RDS instance using other methods such as JDBC or ODBC.
7. For more information on connecting to an Amazon RDS instance, please refer to the [AWS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html).

onelinerhub: [How do I connect to Amazon RDS?](https://onelinerhub.com/amazon-redshift/how-do-i-connect-to-amazon-rds)
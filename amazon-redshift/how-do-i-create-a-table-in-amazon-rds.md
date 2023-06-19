# How do I create a table in Amazon RDS?
// plain

Creating a table in Amazon RDS is a straightforward process. First, you will need to connect to your RDS instance. This can be done with the following code:

```
$ rds-cli configure
```

Once you have connected to your RDS instance, you can create a table with the following SQL command:

```
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  column3 datatype,
  ...
);
```

Here, `table_name` is the name of the table you are creating, and `column1`, `column2`, and `column3` are the names of the columns you are creating, with `datatype` being the data type of the column (e.g. `INT`, `VARCHAR`, etc.).

If the table is successfully created, you will get the following output:

```
Query OK, 0 rows affected (0.04 sec)
```

If you want to learn more about creating tables in Amazon RDS, you can check out the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html).

onelinerhub: [How do I create a table in Amazon RDS?](https://onelinerhub.com/amazon-redshift/how-do-i-create-a-table-in-amazon-rds)
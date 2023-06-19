# How do I use Amazon Redshift to create a tutorial?
// plain

1. Create an Amazon Redshift cluster using the [AWS Console](https://console.aws.amazon.com/redshift/home).
2. Connect to the cluster using a SQL client such as [SQL Workbench/J](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-using-workbench.html).
3. Create a database and a table in your cluster.

```
CREATE DATABASE tutorial;

CREATE TABLE tutorial.users (
  id INTEGER PRIMARY KEY,
  name VARCHAR NOT NULL,
  email VARCHAR NOT NULL
);
```

4. Insert some sample data into the table.

```
INSERT INTO tutorial.users (id, name, email)
VALUES (1, 'John Doe', 'john@example.com'),
       (2, 'Jane Doe', 'jane@example.com');
```

5. Query the table to verify that the data was inserted correctly.

```
SELECT * FROM tutorial.users;

 id |  name  |      email
----+--------+--------------------
  1 | John   | john@example.com
  2 | Jane   | jane@example.com
(2 rows)
```

6. Explain the concepts behind Amazon Redshift and how to use the cluster in a tutorial.
7. Provide additional resources such as [documentation](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-overview.html) and [tutorials](https://aws.amazon.com/getting-started/tutorials/create-cluster-database-redshift/) to help users get started.

onelinerhub: [How do I use Amazon Redshift to create a tutorial?](https://onelinerhub.com/amazon-redshift/how-do-i-use-amazon-redshift-to-create-a-tutorial)
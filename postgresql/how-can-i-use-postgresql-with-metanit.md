# How can I use PostgreSQL with Metanit?
// plain

PostgreSQL is an open-source object-relational database system. It can be used with Metanit to store and manage data in a structured way.

To use PostgreSQL with Metanit, you must first install the PostgreSQL server on your system. You can use the following command to install PostgreSQL on Ubuntu:

```
sudo apt-get install postgresql
```

Once the PostgreSQL server is installed, you can create a database and connect to it using the `psql` command-line interface. For example, to create a database named `mydb` and connect to it, you can use the following commands:

```
createdb mydb
psql mydb
```

Once you are connected to the database, you can use SQL commands to create tables, insert data, and query the database. For example, to create a table named `users`, you can use the following command:

```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
```

You can then insert data into the `users` table using the `INSERT` command:

```
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
```

You can also query the data in the `users` table using the `SELECT` command:

```
SELECT * FROM users;
```

## Output example

```
 id |  name  |      email
----+--------+-----------------
  1 | John Doe | john@example.com
(1 row)
```

To learn more about PostgreSQL and how to use it with Metanit, you can refer to the following resources:

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Metanit Tutorial on PostgreSQL](https://metanit.com/sql/postgresql/1.1.php)

onelinerhub: [How can I use PostgreSQL with Metanit?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-with-metanit)
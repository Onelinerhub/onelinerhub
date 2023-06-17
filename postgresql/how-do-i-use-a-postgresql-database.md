# How do I use a PostgreSQL database?
// plain

PostgreSQL is an open source relational database management system. To use it, you first need to install it on your computer. You can do this by downloading the PostgreSQL installer from the [PostgreSQL website](https://www.postgresql.org/download/).

Once installed, you can access the PostgreSQL shell from your terminal or command line. From there, you can create a database using the `CREATE DATABASE` command. For example:

```
CREATE DATABASE my_database;
```

Once your database is created, you can connect to it using the `\c` command. For example:

```
\c my_database;
```

You can then create tables in your database using the `CREATE TABLE` command. For example:

```
CREATE TABLE people (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
```

You can then insert data into your tables using the `INSERT INTO` command. For example:

```
INSERT INTO people (name, age)
VALUES ('John', 25);
```

You can then query your data using the `SELECT` command. For example:

```
SELECT * FROM people;
```

## Output example

```
 id | name  | age
----+-------+-----
  1 | John  |  25
(1 row)
```

You can find more information about using PostgreSQL in the [PostgreSQL documentation](https://www.postgresql.org/docs/).

onelinerhub: [How do I use a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-use-a-postgresql-database)
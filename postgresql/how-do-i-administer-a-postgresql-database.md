# How do I administer a PostgreSQL database?
// plain

1. First, you need to connect to the PostgreSQL database. To do this, you can use the `psql` command-line interface. For example, to connect to the database named `mydb` with user `postgres`, you can use the following command:

```
psql -U postgres mydb
```

2. Once connected, you can use the `CREATE DATABASE` statement to create a new database. For example:

```
CREATE DATABASE mynewdb;
```

3. You can use the `CREATE TABLE` statement to create tables in the database. For example:

```
CREATE TABLE users (
    id serial primary key,
    name text not null
);
```

4. You can use the `INSERT INTO` statement to add data to the tables. For example:

```
INSERT INTO users (name) VALUES ('John');
```

5. You can use the `SELECT` statement to query the data in the tables. For example:

```
SELECT * FROM users;
```

## Output example

```
id | name
---+------
1  | John
```

6. You can use the `ALTER TABLE` statement to modify the structure of a table. For example:

```
ALTER TABLE users ADD COLUMN email text;
```

7. Finally, you can use the `DROP TABLE` statement to delete tables from the database. For example:

```
DROP TABLE users;
```

For more information on administering PostgreSQL databases, please see the [PostgreSQL documentation](https://www.postgresql.org/docs/).

onelinerhub: [How do I administer a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-administer-a-postgresql-database)
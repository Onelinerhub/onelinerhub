# How do I grant access to a PostgreSQL database?
// plain

1. You can grant access to a PostgreSQL database by using the `GRANT` command.

2. For example, to grant read and write access to a user named `bob` for a database named `mydb`, you would use the following command:

```
GRANT ALL PRIVILEGES ON DATABASE mydb TO bob;
```

3. This command grants `bob` all privileges on the `mydb` database, including the ability to create tables, insert data, and modify data.

4. If you want to grant only read access to `bob`, you can use the following command:

```
GRANT CONNECT ON DATABASE mydb TO bob;
```

5. This command grants `bob` only the ability to connect to the `mydb` database.

6. You can also grant access to specific tables or columns within a database. For example, to grant `bob` read access to a table named `mytable` within `mydb`, you can use the following command:

```
GRANT SELECT ON mytable TO bob;
```

7. For more information about granting access to PostgreSQL databases, see [the PostgreSQL documentation](https://www.postgresql.org/docs/current/sql-grant.html).

onelinerhub: [How do I grant access to a PostgreSQL database?](https://onelinerhub.com/postgresql/how-do-i-grant-access-to-a-postgresql-database)
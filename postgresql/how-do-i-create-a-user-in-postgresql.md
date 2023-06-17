# How do I create a user in PostgreSQL?
// plain

To create a user in PostgreSQL, you must have the necessary privileges to do so.

First, connect to the database server using the `psql` command:

```
$ psql -h localhost -U postgres
```

Then, create a new role with the `CREATE ROLE` command:

```
postgres=# CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword';
CREATE ROLE
```

You can also specify additional options such as the user's privileges, the default database, and the expiration date.

```
postgres=# CREATE ROLE myuser WITH LOGIN PASSWORD 'mypassword' CREATEDB CREATEROLE NOCREATEUSER VALID UNTIL '2021-01-01';
CREATE ROLE
```

The following list explains the meaning of each option used in the example above:

* `LOGIN`: The user will be able to authenticate with the given password.
* `CREATEDB`: The user will be able to create new databases.
* `CREATEROLE`: The user will be able to create new roles.
* `NOCREATEUSER`: The user will not be able to create new users.
* `VALID UNTIL`: The user's account will expire on the given date.

Finally, you can verify that the user was created successfully by using the `\du` command:

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 myuser    | Create DB                                                  | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
```

For more information about creating users in PostgreSQL, you can refer to the official [documentation](https://www.postgresql.org/docs/current/sql-createrole.html).

onelinerhub: [How do I create a user in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-create-a-user-in-postgresql)
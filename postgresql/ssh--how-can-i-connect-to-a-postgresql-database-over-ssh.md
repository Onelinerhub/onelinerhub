# ssh

How can I connect to a PostgreSQL database over SSH?
// plain

You can connect to a PostgreSQL database over SSH using the `psql` command. To do so, you must first establish an SSH connection to the server running the database. To do this, you can use the `ssh` command. For example,

```
$ ssh username@example.com
```

Once the connection is established, you can then connect to the PostgreSQL database using the `psql` command. For example,

```
$ psql -h hostname -d databasename -U username
```

The `-h` option specifies the hostname of the server running the database, the `-d` option specifies the database name, and the `-U` option specifies the username.

Once connected, you can then run SQL queries against the database. For example,

```
$ SELECT * FROM users;
```

This will output the results of the query.

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [SSH Documentation](https://www.ssh.com/ssh/command/)

onelinerhub: [ssh

How can I connect to a PostgreSQL database over SSH?](https://onelinerhub.com/postgresql/ssh--how-can-i-connect-to-a-postgresql-database-over-ssh)
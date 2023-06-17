# How do I get the version of PostgreSQL installed on my system?
// plain

The version of PostgreSQL installed on your system can be obtained by using the `psql` command.

```
psql --version
```

## Output example

```
psql (PostgreSQL) 10.12
```

The `psql` command is used to connect to a PostgreSQL database, and it also provides several options to obtain information about the PostgreSQL installation. The `--version` option prints the version of the PostgreSQL server.

The version of PostgreSQL can also be obtained by using the `SELECT version()` statement.

```
SELECT version();
```

## Output example

```
PostgreSQL 10.12 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-39), 64-bit
```

The `SELECT version()` statement returns the version of the PostgreSQL server, the operating system, and the compiler used to build the server.

To summarize, the version of PostgreSQL installed on your system can be obtained by using the `psql --version` command or the `SELECT version()` statement.

## Helpful links
- [PostgreSQL Documentation - Getting Started](https://www.postgresql.org/docs/current/tutorial-start.html)
- [PostgreSQL Documentation - psql](https://www.postgresql.org/docs/current/app-psql.html)

onelinerhub: [How do I get the version of PostgreSQL installed on my system?](https://onelinerhub.com/postgresql/how-do-i-get-the-version-of-postgresql-installed-on-my-system)
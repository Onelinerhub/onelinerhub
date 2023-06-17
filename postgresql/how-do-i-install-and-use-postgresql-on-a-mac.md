# How do I install and use PostgreSQL on a Mac?
// plain

1. Download and install PostgreSQL from [https://www.postgresql.org/download/macosx/](https://www.postgresql.org/download/macosx/).
2. Open the terminal, and run the following command to start the PostgreSQL server:
```
$ pg_ctl -D /usr/local/var/postgres start
```
3. Create a database:
```
$ createdb mydb
```
4. Connect to the database:
```
$ psql mydb
```
5. Execute SQL queries:
```
mydb=# CREATE TABLE users (
  id serial PRIMARY KEY,
  username VARCHAR (50) UNIQUE NOT NULL,
  password VARCHAR (50) NOT NULL
);
```
6. To check the table, run the following command:
```
mydb=# \d users
```
7. Output:
```
              Table "public.users"
 Column |  Type   | Collation | Nullable | Default
--------+---------+-----------+----------+---------
 id     | integer |           | not null |
 username | character varying(50) | | not null |
 password | character varying(50) | | not null |
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
```

For more information, please refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/).

onelinerhub: [How do I install and use PostgreSQL on a Mac?](https://onelinerhub.com/postgresql/how-do-i-install-and-use-postgresql-on-a-mac)
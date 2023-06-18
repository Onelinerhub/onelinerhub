# How do I show the tables in a SQLite database?
// plain

To show the tables in a SQLite database, you can use the following command:

```
sqlite> .tables
```

This will output a list of all the tables in the database, for example:
```
users  orders  products
```

The `.tables` command is a dot command, which is a special command that begins with a dot (`.`). Dot commands are used to provide meta-information about the database, such as the tables stored in it.

In addition to `.tables`, you can also use `.schema` to show the SQL CREATE statements for all tables in the database. For example:
```
sqlite> .schema
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER);
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT);
```

The `.schema` command is useful for inspecting the structure of the database, such as the column names and data types.

Finally, you can use the `SELECT` statement to query the tables in the database. For example:
```
sqlite> SELECT * FROM users;
1|John
2|Jane
```

This will output the contents of the `users` table.

## Helpful links
- [SQLite Dot Commands](https://www.sqlite.org/cli.html#dot_commands)
- [SQLite SELECT Statement](https://www.sqlite.org/lang_select.html)

onelinerhub: [How do I show the tables in a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-show-the-tables-in-a-sqlite-database)
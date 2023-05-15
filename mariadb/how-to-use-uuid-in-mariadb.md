# How to use UUID in Mariadb?
// plain

UUID stands for Universally Unique Identifier and is a 128-bit number used to identify information in computer systems. In MariaDB, UUIDs can be used to generate unique identifiers for rows in a table.

## Example code

```
CREATE TABLE users (
  id BINARY(16) PRIMARY KEY,
  name VARCHAR(255)
);

INSERT INTO users (id, name) VALUES (UUID(), 'John Doe');
```

## Output example

```
Query OK, 1 row affected (0.00 sec)
```

## Code explanation

- `CREATE TABLE users (id BINARY(16) PRIMARY KEY, name VARCHAR(255));` - creates a table called `users` with two columns, `id` and `name`, where `id` is a binary field of 16 bytes and is set as the primary key.
- `INSERT INTO users (id, name) VALUES (UUID(), 'John Doe');` - inserts a new row into the `users` table, with a unique UUID for the `id` column and `John Doe` for the `name` column.

## Helpful links
- [MariaDB Documentation - UUID](https://mariadb.com/kb/en/library/uuid/)

onelinerhub: [How to use UUID in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-uuid-in-mariadb)
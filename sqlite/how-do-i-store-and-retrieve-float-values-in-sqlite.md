# How do I store and retrieve float values in SQLite?
// plain

Storing and retrieving float values in SQLite is a simple task. To store float values, you can use the `REAL` data type. For example, the following SQL statement creates a table with a float column:

```sql
CREATE TABLE mytable (
    id INTEGER PRIMARY KEY,
    value REAL
);
```

To insert float values into the table, use the `INSERT INTO` statement:

```sql
INSERT INTO mytable (value) VALUES (3.14);
```

To retrieve float values from the table, use the `SELECT` statement:

```sql
SELECT * FROM mytable;
```

The output would look something like this:

```
id    value
1     3.14
```

## Code explanation


- `CREATE TABLE` statement - used to create a table with a float column
- `INSERT INTO` statement - used to insert float values into the table
- `SELECT` statement - used to retrieve float values from the table

Here are some ## Helpful links

- [SQLite Data Types](https://www.sqlitetutorial.net/sqlite-data-types/)
- [SQLite INSERT](https://www.sqlitetutorial.net/sqlite-insert/)
- [SQLite SELECT](https://www.sqlitetutorial.net/sqlite-select/)

onelinerhub: [How do I store and retrieve float values in SQLite?](https://onelinerhub.com/sqlite/how-do-i-store-and-retrieve-float-values-in-sqlite)
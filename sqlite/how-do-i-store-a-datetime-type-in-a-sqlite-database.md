# How do I store a datetime type in a SQLite database?
// plain

Storing a datetime type in a SQLite database can be done using the **DATETIME** data type. Below is an example of how to store a datetime type in a SQLite database. The example code creates a table called "events" with a column called "date" of type DATETIME and inserts a datetime value into it.

```
CREATE TABLE events (date DATETIME);
INSERT INTO events VALUES (datetime('now'));
```

## Code explanation


1. `CREATE TABLE events (date DATETIME)`: This creates a table called "events" with a column called "date" of type DATETIME.
2. `INSERT INTO events VALUES (datetime('now'))`: This inserts a datetime value into the "events" table.

## Helpful links

- [SQLite Data Types](https://www.sqlite.org/datatype3.html)
- [SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)

onelinerhub: [How do I store a datetime type in a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-store-a-datetime-type-in-a-sqlite-database)
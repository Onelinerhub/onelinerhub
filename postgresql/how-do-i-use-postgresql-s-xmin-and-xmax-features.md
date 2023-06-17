# How do I use PostgreSQL's XMIN and XMAX features?
// plain

PostgreSQL's XMIN and XMAX features are used to track and manage data changes in a transaction. XMIN and XMAX are special columns that are automatically added to every table when the transaction is started.

XMIN is used to track the transaction that inserted a row into the table, while XMAX is used to track the transaction that deleted or updated the row. When a transaction is committed, the XMIN and XMAX values are set to the transaction's ID.

## Example code

```
BEGIN;

INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);

SELECT * FROM table_name;

```

## Output example

```
 id | xmin | xmax | column1 | column2
----+------+------+---------+---------
  1 |    0 |    0 | value1  | value2
```

The code above starts a transaction, inserts a row into the table, and then selects all the rows from the table. The output shows that the XMIN and XMAX values are both set to 0, indicating that the row was inserted in the current transaction.

When the transaction is committed, the XMIN and XMAX values will be set to the transaction's ID:

```
COMMIT;

SELECT * FROM table_name;
```

## Output example

```
 id | xmin | xmax | column1 | column2
----+------+------+---------+---------
  1 |   42 |    0 | value1  | value2
```

The output shows that the XMIN value is set to the transaction's ID (42), and the XMAX value is still 0, indicating that the row was inserted in the current transaction.

## Code explanation

- BEGIN;: Starts a new transaction.
- INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);: Inserts a row into the table.
- SELECT * FROM table_name;: Selects all the rows from the table.
- COMMIT;: Commits the transaction.

## Helpful links
- [PostgreSQL Documentation - XMIN and XMAX](https://www.postgresql.org/docs/current/ddl-system-columns.html#DDL-SYS-COLUMNS-XMIN-XMAX)

onelinerhub: [How do I use PostgreSQL's XMIN and XMAX features?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-xmin-and-xmax-features)
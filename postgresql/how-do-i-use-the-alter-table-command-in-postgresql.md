# How do I use the ALTER TABLE command in PostgreSQL?
// plain

The ALTER TABLE command in PostgreSQL is used to modify existing tables in the database. It can be used to add, modify, or delete columns, change the data type of columns, add or remove constraints, and rename tables.

## Example code

```
ALTER TABLE orders
ADD COLUMN order_date date;
```

This example code adds a new column called 'order_date' to the 'orders' table with a data type of 'date'.

The parts of the code are:
- ALTER TABLE: This is the command used to modify existing tables.
- orders: This is the name of the table to be modified.
- ADD COLUMN: This is the action being taken on the table.
- order_date: This is the name of the new column being added.
- date: This is the data type of the new column being added.

## Helpful links
- [PostgreSQL Documentation: ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)
- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)

onelinerhub: [How do I use the ALTER TABLE command in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-the-alter-table-command-in-postgresql)
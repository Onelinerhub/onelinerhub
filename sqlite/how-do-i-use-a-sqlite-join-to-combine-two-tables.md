# How do I use a SQLite join to combine two tables?
// plain

A SQLite join is used to combine two tables by combining their columns. The syntax for a join is as follows:

```
SELECT <columns_to_select>
FROM <table1>
JOIN <table2>
ON <table1>.<column> = <table2>.<column>;
```

The `SELECT` clause is used to specify which columns you want to view from the two tables. The `FROM` clause is used to specify which tables you want to join. The `JOIN` clause is used to specify how the two tables are to be joined. The `ON` clause is used to specify which columns are used to match up the two tables. For example, if you have two tables named `customers` and `orders`, you could join them together like this:

```
SELECT customers.name, orders.order_date
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

This would return the names of customers and the dates of their orders.

Parts of the code:
- `SELECT` clause: used to specify which columns to view from the two tables
- `FROM` clause: used to specify which tables to join
- `JOIN` clause: used to specify how the two tables are to be joined
- `ON` clause: used to specify which columns are used to match up the two tables

## Helpful links
- [SQLite Joins](https://www.sqlitetutorial.net/sqlite-join/)
- [SQLite SELECT](https://www.sqlitetutorial.net/sqlite-select/)

onelinerhub: [How do I use a SQLite join to combine two tables?](https://onelinerhub.com/sqlite/how-do-i-use-a-sqlite-join-to-combine-two-tables)
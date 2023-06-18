# How do I use a LEFT JOIN in SQLite?
// plain

A LEFT JOIN in SQLite is used to combine data from two tables, where data from the left table is returned based on a match with data from the right table. The syntax for a LEFT JOIN in SQLite is:

```
SELECT column1, column2, ...
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

For example, if we have two tables `customers` and `orders`, we can join them together using the following code:

```
SELECT customers.name, orders.order_date
FROM customers
LEFT JOIN orders
ON customers.customer_id = orders.customer_id;
```

The code above will return all customers from the `customers` table, even if there is no matching order in the `orders` table.

The parts of the LEFT JOIN statement are:

- SELECT: This is used to specify which columns from the tables should be returned.
- FROM: This is used to specify which table should be used as the left table.
- LEFT JOIN: This is used to specify that a LEFT JOIN should be used.
- ON: This is used to specify the condition that should be used to join the two tables.

## Helpful links
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQLite LEFT JOIN](https://www.sqlite.org/lang_select.html#leftjoin)

onelinerhub: [How do I use a LEFT JOIN in SQLite?](https://onelinerhub.com/sqlite/how-do-i-use-a-left-join-in-sqlite)
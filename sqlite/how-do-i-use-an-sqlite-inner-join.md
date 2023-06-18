# How do I use an SQLite inner join?
// plain

An SQLite inner join is used to combine data from two or more tables in a database. It returns all rows from multiple tables where the join condition is met. The syntax for an inner join is as follows:

```
SELECT table1.column1, table2.column2
FROM table1
INNER JOIN table2
ON table1.common_field = table2.common_field;
```

The SELECT statement specifies the columns that are returned in the result set, the FROM clause specifies the tables that are used in the query, the INNER JOIN clause joins the two tables together on a common field, and the ON clause specifies the condition for the join.

For example, if we have two tables, "Customers" and "Orders", and we want to join the two tables together based on the "CustomerID" field, we could use the following query:

```
SELECT Customers.Name, Orders.OrderDate
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

The output of this query might look something like this:

```
John Smith, 2020-01-01
Jane Doe, 2020-02-01
```

## Code explanation


- SELECT table1.column1, table2.column2: This specifies the columns that are returned in the result set.

- FROM table1: This specifies the first table that is used in the query.

- INNER JOIN table2: This specifies the type of join (in this case, an inner join).

- ON table1.common_field = table2.common_field: This specifies the condition for the join.

## Helpful links

- [SQLite Inner Join](https://www.sqlitetutorial.net/sqlite-inner-join/)
- [SQLite Joins](https://www.sqlitetutorial.net/sqlite-joins/)

onelinerhub: [How do I use an SQLite inner join?](https://onelinerhub.com/sqlite/how-do-i-use-an-sqlite-inner-join)
# How can I use PostgreSQL's "zero if null" feature?
// plain

PostgreSQL's "zero if null" feature is a conditional expression that allows you to replace NULL values with a specified value. This is especially useful when working with aggregate functions such as SUM, AVG, or COUNT, which return NULL when there are no matching rows.

For example, the following code block will retrieve the total number of orders from the orders table, replacing any NULL values with 0:

```
SELECT SUM(orders) AS total_orders FROM orders WHERE orders IS NOT NULL OR orders = 0;
```

The output of this query will be the total number of orders, with any NULL values replaced by 0.

The code can be broken down into the following parts:

* SELECT: This keyword is used to retrieve data from the database.
* SUM(): This function is used to calculate the sum of the orders.
* orders: This is the column containing the orders data.
* AS total_orders: This keyword is used to assign an alias to the result of the SUM() function.
* WHERE orders IS NOT NULL: This clause is used to filter out any rows with NULL values.
* OR orders = 0: This clause is used to replace any NULL values with 0.

For more information on PostgreSQL's "zero if null" feature, please see the following links:

* [PostgreSQL Documentation](https://www.postgresql.org/docs/12/functions-conditional.html)
* [PostgreSQL Tutorial](https://www.postgresqltutorial.com/postgresql-null-values/)

onelinerhub: [How can I use PostgreSQL's "zero if null" feature?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-s--zero-if-null--feature)
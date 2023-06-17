# How do I use PostgreSQL aggregate functions?
// plain

PostgreSQL aggregate functions allow you to perform calculations on multiple rows of data and return a single result. To use an aggregate function, you must specify the name of the function followed by the column or expression that you want to use in the calculation.

For example, to calculate the total salary of all employees in a table, you can use the `SUM` aggregate function:

```
SELECT SUM(salary)
FROM employees;
```

The output of this query would be a single number representing the total salary of all employees.

The syntax for using an aggregate function is as follows:

```
SELECT <aggregate_function>(<column_or_expression>)
FROM <table_name>;
```

The following is a list of the most commonly used PostgreSQL aggregate functions:

1. `SUM`: Calculates the sum of a column or expression.
2. `AVG`: Calculates the average of a column or expression.
3. `MIN`: Returns the minimum value of a column or expression.
4. `MAX`: Returns the maximum value of a column or expression.
5. `COUNT`: Counts the number of rows in a table.

For more information, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/functions-aggregate.html).

onelinerhub: [How do I use PostgreSQL aggregate functions?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-aggregate-functions)
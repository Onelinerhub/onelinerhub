# How to use window functions in Mariadb?
// plain

Window functions in MariaDB are used to perform calculations over a set of rows that are related to the current row. They are similar to aggregate functions, but allow for the calculation to be done over a subset of the rows in the table.

## Example


```
SELECT id, name,
       AVG(salary) OVER (PARTITION BY dept_id) AS avg_salary
FROM employees
```

This example will calculate the average salary for each department. The `PARTITION BY` clause defines the subset of rows to be used for the calculation.

## Code explanation


- `SELECT`: specifies the columns to be returned in the result set
- `AVG()`: the window function used to calculate the average salary
- `OVER`: specifies the window for the calculation
- `PARTITION BY`: defines the subset of rows to be used for the calculation

## Helpful links

- [Window Functions in MariaDB](https://mariadb.com/kb/en/library/window-functions/)
- [Window Functions in MariaDB 10.3](https://mariadb.com/kb/en/library/window-functions-in-mariadb-103/)

onelinerhub: [How to use window functions in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-window-functions-in-mariadb)
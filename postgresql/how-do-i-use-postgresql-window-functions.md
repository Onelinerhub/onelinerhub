# How do I use PostgreSQL window functions?
// plain

PostgreSQL window functions are used to perform calculations over a set of rows. They are analogous to aggregate functions, but operate on a subset of the rows in the result set.

## Example code

```
SELECT
    id,
    name,
    salary,
    avg(salary) OVER (ORDER BY id)
FROM
    employees
ORDER BY
    id;
```

## Output example

```
 id |   name   | salary |     avg
----+----------+--------+--------------
  1 | John     |   5000 | 5000.00000000
  2 | Mary     |   6000 | 5250.00000000
  3 | Bob      |   7000 | 5500.00000000
  4 | Sarah    |   8000 | 6500.00000000
  5 | David    |   9000 | 7250.00000000
```

The code above calculates the average salary for each employee using a window function. The `OVER` clause specifies the window frame, which is the set of rows over which the calculation will be performed. In this example, the window frame is all rows ordered by the `id` column.

The `avg()` function is used to calculate the average salary for each employee. The `ORDER BY` clause ensures that the window frame is ordered correctly, so that the calculation is performed in the correct order.

For more information about PostgreSQL window functions, see the following links:

- [PostgreSQL Documentation: Window Functions](https://www.postgresql.org/docs/current/tutorial-window.html)
- [PostgreSQL Window Functions Tutorial](https://www.postgresqltutorial.com/postgresql-window-functions/)

onelinerhub: [How do I use PostgreSQL window functions?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-window-functions)
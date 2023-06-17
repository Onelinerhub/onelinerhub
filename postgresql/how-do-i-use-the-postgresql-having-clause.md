# How do I use the PostgreSQL HAVING clause?
// plain

The PostgreSQL HAVING clause is used to filter the result set of a SELECT statement based on grouping. It is used in conjunction with GROUP BY to filter the results of aggregate functions.

For example, the following query will show the average salary of each department:

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

## Output example

```
Department  AVG(salary)
IT          50000
Sales       60000
Marketing   65000
```

The HAVING clause can be used to filter the result set further. For example, the following query will show the average salary of each department with a salary greater than $60,000:

```
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

## Output example

```
Department  AVG(salary)
Marketing   65000
```

The parts of the query are:

1. SELECT: This clause specifies the columns to be included in the result set.
2. FROM: This clause specifies the table from which the data is selected.
3. GROUP BY: This clause groups the rows by the specified column.
4. HAVING: This clause filters the result set based on the specified condition.

For more information, please refer to the following link:

[PostgreSQL Documentation - HAVING Clause](https://www.postgresql.org/docs/9.6/sql-select.html#SQL-HAVING)

onelinerhub: [How do I use the PostgreSQL HAVING clause?](https://onelinerhub.com/postgresql/how-do-i-use-the-postgresql-having-clause)
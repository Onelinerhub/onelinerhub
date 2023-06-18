# How can I use the GROUP BY clause in SQLite?
// plain

The GROUP BY clause in SQLite is used to group together rows of data based on a given field or expression. It is used in conjunction with aggregate functions such as COUNT, SUM, AVG, MIN and MAX.

For example, the following query groups the data by the 'department' field and returns the total number of employees in each department:

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

## Output example

```
department  COUNT(*)
----------  --------
sales            10
marketing        5
engineering      15
```

The query consists of the following parts:

- SELECT: The SELECT clause specifies the fields to be returned in the result set. In this case, it is the 'department' field and the COUNT aggregate function.

- FROM: The FROM clause specifies the table from which to retrieve the data. In this case, it is the 'employees' table.

- GROUP BY: The GROUP BY clause specifies the field or expression by which to group the data. In this case, it is the 'department' field.

- COUNT: The COUNT aggregate function returns the number of rows in each group.

## Helpful links

- [SQLite Group By](https://www.sqlitetutorial.net/sqlite-group-by/)
- [SQLite Aggregate Functions](https://www.sqlitetutorial.net/sqlite-aggregate-functions/)

onelinerhub: [How can I use the GROUP BY clause in SQLite?](https://onelinerhub.com/sqlite/how-can-i-use-the-group-by-clause-in-sqlite)
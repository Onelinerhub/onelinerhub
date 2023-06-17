# How do I use the EXISTS keyword in PostgreSQL?
// plain

The EXISTS keyword in PostgreSQL is used to check if a row or rows exist in a table. It is commonly used in a subquery to determine whether a row exists in a table or not. EXISTS returns true if at least one row is found in the table, otherwise it returns false.

## Example


```
SELECT *
FROM table1
WHERE EXISTS (SELECT *
              FROM table2
              WHERE table1.id = table2.id);
```

This query will return all the rows from table1 where the id from table1 matches the id from table2.

## Code explanation


1. SELECT * - This part of the code selects all the columns from the table.
2. FROM table1 - This part of the code specifies which table the query should look into.
3. WHERE EXISTS - This part of the code checks if a row or rows exist in the table.
4. (SELECT * - This part of the code selects all the columns from the table.
5. FROM table2 - This part of the code specifies which table the query should look into.
6. WHERE table1.id = table2.id) - This part of the code checks if the id from table1 matches the id from table2.

## Helpful links

1. [PostgreSQL Documentation on EXISTS](https://www.postgresql.org/docs/9.1/functions-subquery.html#FUNCTIONS-EXISTS)
2. [PostgreSQL Tutorial on EXISTS](https://www.postgresqltutorial.com/postgresql-exists/)

onelinerhub: [How do I use the EXISTS keyword in PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-use-the-exists-keyword-in-postgresql)
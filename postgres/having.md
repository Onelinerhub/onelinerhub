# How to filter resulting set after grouping is done

```sql
SELECT first_name, COUNT(*) AS count FROM person GROUP BY first_name HAVING count >= 2;
```
- first_name, COUNT(\*) AS count - select the column `first_name` and apply an aggregate function named `COUNT()` on every row from all columns that counts the number of rows and name this column `count`
- GROUP BY first_name - group the result set by `first_name`
- HAVING count >= 2 - return only the rows that have 2 or more occurrences of the same `first_name `

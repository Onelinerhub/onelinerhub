# Having

```sql
SELECT first_name, COUNT(*) FROM person GROUP BY first_name HAVING COUNT(*) >= 2;
```
- \\* - refers to every column in table person
- COUNT(*) - aggregate function that returns the number of rows
- GROUP BY first_name - group the result set by first_name
- HAVING COUNT(*) >= 2 - return only the rows that have 2 or more occurrences of the same first_name 
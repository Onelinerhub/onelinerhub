# Group By

```sql
SELECT first_name, COUNT(*) FROM person GROUP BY first_name;
```
- \\* - refers to every column in table person
- COUNT(*) - aggregate function that returns the number of rows
- GROUP BY first_name - group the result set by first_name
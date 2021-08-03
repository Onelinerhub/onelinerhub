# How to group resulting set by specific column values

```sql
SELECT first_name, COUNT(*) FROM person GROUP BY first_name;
```
- COUNT(\*) - aggregate function that returns the number of rows
- GROUP BY first_name - group the result set by first_name

# How to find duplicate varchar/text column values in table

```sql
SELECT name, count(*) total FROM table GROUP BY name HAVING total > 1;
```

- SELECT name - let's assume this column is the one to find duplicates for
- count(*) total - find total number of same values of ```name``` column
- table - our table name
- GROUP BY name - grouping will return only unique values of ```name``` column
- HAVING total > 1 - will filter only those ```name``` values that have duplicates (occur more than once)

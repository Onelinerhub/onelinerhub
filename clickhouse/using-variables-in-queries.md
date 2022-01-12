# Using variables in queries

```sql
WITH '2020' AS min_year SELECT * FROM tbl WHERE toYear(date) > min_year
```

- `WITH` - allows defining user variables
- `'2020'` - user variable value
- `min_year` - user variable name
- `SELECT * FROM tbl` - sample select

group: with

## Example: 
```sql
WITH '2020' AS min_year SELECT * FROM tbl WHERE toYear(date) > min_year
```
```
┌───────date─┬─col────┬─val─┬─age─┐
│ 2022-01-07 │ Donald │   0 │   0 │
│ 2022-01-10 │ Donald │   0 │   0 │
│ 2022-01-11 │ Donald │   0 │   0 │
...
```


# Using groupArray in queries

```sql
SELECT date, groupArray(col) FROM tbl GROUP BY date
```

- `tbl` - table to select data from
- `date` - column to group by
- `groupArray` - will group all column values into an array
- `col` - column which values to group into an array

## Example: 
```sql
SELECT date, groupArray(col) FROM tbl GROUP BY date
```
```
┌───────date─┬─groupArray(col)─────────────────────────────────────────────────────────────────────────────┐
│ 1970-01-01 │ ['hi','Donald','hi','Donald','hi','Donald','hi','Donald','hi','Donald']                     │
│ 2022-01-07 │ ['Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald'] │
│ 2022-01-10 │ ['Donald','Donald','Donald','Donald','Donald']                                              │
│ 2022-01-11 │ ['Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald','Donald'] │
│ 2022-01-12 │ ['Donald','Donald','Donald','Donald','Donald']                                              │
│ 2022-01-14 │ ['hi','good']                                                                               │
└────────────┴─────────────────────────────────────────────────────────────────────────────────────────────┘

```


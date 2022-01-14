# Using anyLast() with grouped data

```sql
SELECT date, anyLast(col) FROM tbl GROUP BY date
```

- `anyLast(` - select last fetched value of specified column
- `col` - column to select value for
- `tbl` - standard table to select data from
- `date` - column to group by

group: any

## Example: 
```sql
SELECT date, anyLast(col) FROM tbl GROUP BY date
```
```
┌───────date─┬─anyLast(col)─┐
│ 1970-01-01 │ Donald       │
│ 2022-01-07 │ Donald       │
│ 2022-01-10 │ Donald       │
│ 2022-01-11 │ Donald       │
│ 2022-01-12 │ Donald       │
└────────────┴──────────────┘
```


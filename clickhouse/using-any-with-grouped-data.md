# Using any() with grouped data

```sql
SELECT date, any(col) FROM tbl GROUP BY date
```

- `any(` - select first fetched value of specified column
- `col` - column to select value for
- `tbl` - standard table to select data from
- `date` - column to group by

group: any

## Example: 
```sql
SELECT date, any(col) FROM tbl GROUP BY date
```
```
┌───────date─┬─any(col)─┐
│ 1970-01-01 │ hi       │
│ 2022-01-07 │ Donald   │
│ 2022-01-10 │ Donald   │
│ 2022-01-11 │ Donald   │
│ 2022-01-12 │ Donald   │
└────────────┴──────────┘
```


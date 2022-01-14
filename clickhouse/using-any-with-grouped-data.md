# Using any() with grouped data

```sql
SELECT date, any(col) FROM tbl GROUP BY date
```

- `any(` - select first fetched value of specified column
- `col` - column to select value for
- `tbl` - standard table to select data from
- `date` - column to group by

group: any



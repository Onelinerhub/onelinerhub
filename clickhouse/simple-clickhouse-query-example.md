# Simple Clickhouse query example

```sql
SELECT count(*) total, date FROM tbl GROUP BY date ORDER BY total DESC
```

- `count(*) total, date` - columns to select (aggregate count and `date` in our case)
- `tbl` - table to select from
- `GROUP BY date` - group our result set by `date` column
- `ORDER BY total DESC` - sort our result set by `total` (count), biggest value on top

## Example: 
```sql
SELECT count(*) total, date FROM tbl GROUP BY date ORDER BY total DESC
```
```
┌─total─┬───────date─┐
│     2 │ 2022-01-11 │
│     1 │ 2022-01-07 │
│     1 │ 2022-01-10 │
│     1 │ 2022-01-12 │
└───────┴────────────┘
```


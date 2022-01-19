# LEFT JOIN query example

```sql
SELECT * FROM tbl1 t1 LEFT JOIN tbl2 t2 ON (t1.id = t2.event_id)
```

- `tbl1 t1` - first table with alias
- `tbl2 t2` - second table to join to `tbl1`
- `LEFT JOIN` - will select all rows from `tbl1` and matched rows from `tbl2` (or empty values if no match)
- `ON` - condition to join rows from specified tables
- `t1.id = t2.event_id` - will select all rows from `tbl2` where `event_id` column is equal to `id` column of `tbl1` 

group: joins



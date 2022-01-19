# JOIN query example

```sql
SELECT * FROM tbl1 t1 JOIN tbl2 t2 ON (t1.id = t2.event_id)
```

- `tbl1 t1` - first table with alias
- `tbl2 t2` - second table to join to `tbl1`
- `JOIN` - will select rows matching `tbl1` and `tbl2`
- `ON` - condition to join rows from specified tables
- `t1.id = t2.event_id` - will select all rows from `tbl2` where `event_id` column is equal to `id` column of `tbl1` 

group: joins



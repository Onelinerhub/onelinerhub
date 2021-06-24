# Select first record from group

```sql
SELECT id, name FROM table WHERE id IN ( SELECT min(id) FROM table GROUP BY name )
```

- SELECT id, name - columns to select
- table - table name to select from
- WHERE id IN - select only certain ids, defined by subquery
- SELECT min(id) FROM table GROUP BY name - subqyery will return first (minimum) ids for each unique ```name``` value

group: record_order

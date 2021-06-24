# Select last record from group

```sql
SELECT id, name FROM table WHERE id IN ( SELECT max(id) FROM table GROUP BY name )
```

- SELECT id, name - columns to select
- table - table name to select from ([definition](/mysql/create_table))
- WHERE id IN - select only certain ids, defined by subquery
- SELECT max(id) FROM table GROUP BY name - subqyery will return last (maximum) ids for each unique ```name``` value

group: record_order

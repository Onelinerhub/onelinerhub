# Selecting data from ReplacingMergeTree table

```sql
SELECT * FROM rt FINAL;
```

- `rt` - name of the [ReplacingMergeTree table](/clickhouse/create-replacingmergetree-table)
- `FINAL` - will show only latest versions of all rows

group: ReplacingMergeTree

## Example: 
```sql
SELECT * FROM rt FINAL;
```
```
┌─id─┬─ver─┬─name────┐
│  1 │   3 │ Hillary │
└────┴─────┴─────────┘

```


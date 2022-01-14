# Update rows in ReplacingMergeTree table

```sql
INSERT INTO rt(id, ver, name) VALUES(1, 3, 'Hillary')
```

- `rt` - name of the [ReplacingMergeTree table](/clickhouse/create-replacingmergetree-table)
- `id` - primary key column (identifies unique rows)
- `ver` - version column (we should increment it to overwrite row identified by `id`)
- `name` - sample string column
- `(1, 3, 'Hillary')` - we insert `3` into `ver` column (assume current version stored there is `2`)

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


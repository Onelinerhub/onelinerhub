# Create ReplacingMergeTree table

```sql
CREATE TABLE rt(id UInt32, ver UInt8, name String) ENGINE = ReplacingMergeTree(ver) ORDER BY id
```

- `rt` - name of the ReplacingMergeTree table to create
- `id UInt32` - column to be used in primary key
- `ver UInt8` - version column
- `name String` - sample string column
- `(ver)` - name of the version column
- `ORDER BY id` - unique key expression (`id` column in our case)

group: ReplacingMergeTree



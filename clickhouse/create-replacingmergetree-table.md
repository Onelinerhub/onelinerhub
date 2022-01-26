# Create ReplacingMergeTree table

```sql
CREATE TABLE rt(id UInt32, ver UInt8, name String) ENGINE = ReplacingMergeTree(ver) ORDER BY id
```

- `rt` - name of the ReplacingMergeTree table to create
- `id UInt32` - column to be used as a primary key
- `ver UInt8` - version column (increment it to overwrite row identified by primary key)
- `name String` - sample string column
- `(ver)` - name of the version column
- `ORDER BY id` - primary key (unique row identification) expression (`id` column in our case)

group: ReplacingMergeTree

## Example: 
```sql
CREATE TABLE rt(id UInt32, ver UInt8, name String) ENGINE = ReplacingMergeTree(ver) ORDER BY id;
INSERT INTO rt VALUES(1, 1, 'Donald');
INSERT INTO rt VALUES(1, 2, 'Joe');
SELECT * FROM rt FINAL;
```
```
┌─id─┬─ver─┬─name─┐
│  1 │   2 │ Joe  │
└────┴─────┴──────┘
```

link_youtube: https://youtu.be/RKv0THlTI8Y

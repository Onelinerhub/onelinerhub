# How to insert Tuple values

```sql
INSERT INTO tbl4 (ts, person) VALUES(now(), ('Donald', 1))
```

- `tbl4` - name of the table with Tuple column
- `person` - name of the [created Tuple column](/clickhouse/how-to-create-tuple-column)
- `('Donald', 1)` - Tuple column value consisting of a `String` and `UInt32`

group: tuple

## Example: 
```sql
INSERT INTO tbl4 (ts, person) VALUES(now(), ('Donald', 1));
SELECT * FROM tbl4;
```
```
┌──────────────────ts─┬─person───────┐
│ 2022-01-19 14:04:03 │ ('Donald',1) │
└─────────────────────┴──────────────┘
```

link_youtube: https://youtu.be/naTWg13gbl4

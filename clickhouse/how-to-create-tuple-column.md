# How to create Tuple column

```sql
CREATE TABLE tbl4 ( `ts` DateTime, `person` Tuple(name String, code UInt32) ) ENGINE = MergeTree ORDER BY ts
```

- `tbl4` - name of the table with Tuple column
- `person` - name of the Tuple column
- `Tuple(` - declares Tuple
- `name String` - first variable in a Tuple named `name` and of `String` type
- `code UInt32` - second variable in a Tuple named `code` and on `UInt32` type

group: tuple


link_youtube: https://youtu.be/vI_K9rPVf_s

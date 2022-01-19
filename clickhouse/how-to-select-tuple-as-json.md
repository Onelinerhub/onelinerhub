# How to select Tuple as JSON

```sql
SELECT toJSONString(person) FROM tbl4
```

- `tbl4` - name of the table with Tuple column
- `person` - name of the [created Tuple column](/clickhouse/how-to-create-tuple-column)
- `toJSONString` - will convert Tuple values to JSON strings (as arrays)

group: tuple

## Example: 
```sql
SELECT toJSONString(person) FROM tbl4
```
```
┌─toJSONString(person)─┐
│ ["Donald",1]         │
│ ["Joe",2]            │
└──────────────────────┘
```


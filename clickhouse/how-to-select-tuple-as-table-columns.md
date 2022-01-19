# How to select Tuple as table columns

```sql
SELECT untuple(person) FROM tbl4
```

- `tbl4` - name of the table with Tuple column
- `person` - name of the [created Tuple column](/clickhouse/how-to-create-tuple-column)
- `untuple` - will expand tuple elements to table columns in a result set

group: tuple

## Example: 
```sql
SELECT untuple(person) FROM tbl4
```
```
┌─tupleElement(person, 1)─┬─tupleElement(person, 2)─┐
│ Donald                  │                       1 │
│ Joe                     │                       2 │
└─────────────────────────┴─────────────────────────┘

```


# How to select based on tuple element value

```sql
SELECT * FROM tbl4 WHERE person.name = 'Joe'
```

- `tbl4` - name of the table with Tuple column
- `person` - name of the [created Tuple column](/clickhouse/how-to-create-tuple-column)
- `.name` - name of the Tuple element
- `'Joe'` - value to search for in `person.name`

group: tuple

## Example: 
```sql
SELECT * FROM tbl4 WHERE person.name = 'Joe';
```
```
┌──────────────────ts─┬─person────┐
│ 2022-01-19 14:04:09 │ ('Joe',2) │
└─────────────────────┴───────────┘

```


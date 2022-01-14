# Select rows with all specified values in array column

```sql
SELECT * FROM tbl3 WHERE hasAll(list, ['b', 'd'])
```

- `tbl3` - table with [array column in it](/clickhouse/create-array-column)
- `hasAll` - will return `true` if specified array column has all specified values in it
- `list` - name of the array column
- `['b', 'd']` - values to search in array column

group: array

## Example: 
```sql
SELECT * FROM tbl3 WHERE hasAll(list, ['b', 'd'])
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘
```


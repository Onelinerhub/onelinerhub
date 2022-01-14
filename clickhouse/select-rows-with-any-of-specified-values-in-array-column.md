# Select rows with any of specified values in array column

```sql
SELECT * FROM tbl3 WHERE hasAny(list, ['a', 'd'])
```

- `tbl3` - table with [array column in it](/clickhouse/create-array-column)
- `hasAny` - will return `true` if specified array column has any of specified values in it
- `list` - name of the array column
- `['a', 'd']` - values to search in array column

group: array

## Example: 
```sql
SELECT * FROM tbl3 WHERE hasAny(list, ['a', 'd'])
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:32 │ ['a','b','c'] │
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘
```


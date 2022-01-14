# Select rows with certain value in array column

```sql
SELECT * FROM tbl3 WHERE has(list, 'd')
```

- `tbl3` - table with array column
- `has` - will return `true` if specified array column has specified value in it
- `list` - name of the array column
- `'d'` - value to search in array

group: array

## Example: 
```sql
SELECT * FROM tbl3 WHERE has(list, 'd')
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘
```


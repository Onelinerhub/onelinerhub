# Insert value into array column

```sql
INSERT INTO tbl3(ts, list) VALUES(now(), ['a', 'b', 'c'])
```

- `tbl3` - table [with array column](/clickhouse/create-array-column)
- `list` - name of array (of strings) column
- `['a', 'b', 'c']` - value for array column

group: array

## Example: 
```sql
INSERT INTO tbl3(ts, list) VALUES(now(), ['a', 'b', 'c']);
SELECT * FROM tbl3;
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:32 │ ['a','b','c'] │
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘
```


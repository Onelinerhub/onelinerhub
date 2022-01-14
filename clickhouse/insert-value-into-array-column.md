# Insert value into array column

```sql
INSERT INTO tbl3(ts, list) VALUES(now(), ['a', 'b', 'c'])
```

- `tbl3` - name of the table with array column to create
- `list` - name of the array column
- `Array(String)` - this will be array of strings

group: array

## Example: 
```sql
INSERT INTO tbl3(ts, list) VALUES(now(), ['a', 'b', 'c']);
SELECT * FROM tbl3;
```
```
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:32 │ ['a','b','c'] │
└─────────────────────┴───────────────┘
┌──────────────────ts─┬─list──────────┐
│ 2022-01-14 17:41:38 │ ['b','c','d'] │
└─────────────────────┴───────────────┘
```


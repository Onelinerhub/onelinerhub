# How to copy table

```lua
tbl_copy = {table.unpack(tbl)}
```

- `table.clone` - will duplicate given table
- `tbl` - table to copy
- `tbl_copy` - variable with a new table copied from given

## Example: 
```lua
tbl = {1, 2, 3}
tbl_copy = {table.unpack(tbl)}

table.insert(tbl_copy, 4);

print(table.concat(tbl, ','))
print(table.concat(tbl_copy, ','))
```
```
1,2,3
1,2,3,4

```


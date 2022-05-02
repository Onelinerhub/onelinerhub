# How to copy table

```lua
tbl_copy = {table.unpack(tbl)}
```

- `table.unpack` - return list of table items instead of the table itself
- `tbl` - table to copy
- `tbl_copy` - variable with a new table copied from given

group: table_manage

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

link_youtube: https://youtu.be/-pzSYAtCFGo

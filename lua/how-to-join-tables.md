# How to join tables

### This approach will append all items from second table to the first one:

```lua
for k,v in pairs(tbl2) do
  table.insert(tbl1, v)
end
```

- `for k,v in pairs(tbl2)` - iterate through all elements of second table
- `tbl2` - second table to add to first one
- `tbl1` - first table to join with second
- `table.insert` - will append given value to the given table

group: table_manage

## Example: 
```lua
tbl1 = {1, 2, 3}
tbl2 = {4, 5}
for k,v in pairs(tbl2) do
  table.insert(tbl1, v)
end

print(table.concat(tbl1, ' '))
```
```
1 2 3 4 5

```

link_youtube: https://youtu.be/xw6AOh5-nA0

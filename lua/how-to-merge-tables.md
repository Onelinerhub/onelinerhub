# How to merge tables

### This approach will overwrite all items from the first table with corresponding values from the second one (and append all values from second table which are absent in first):

```lua
for k,v in pairs(tbl2) do
  tbl1[k] = v
end
```

- `for k,v in pairs(tbl2)` - iterate through all elements of second table
- `tbl2` - second table to add to first one
- `tbl1` - first table to join with second
- `tbl1[k] = v` - set given `v` value at `k` position of `tbl1` table

group: table_manage

## Example: 
```lua
tbl1 = {1, 2, 3}
tbl2 = {4, 5}
for k,v in pairs(tbl2) do
  tbl1[k] = v
end

print(table.concat(tbl1, ' '))
```
```
4 5 3

```

link_youtube: https://youtu.be/skcQQvvzXI8

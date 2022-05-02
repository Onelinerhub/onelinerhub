# How to add item to table

```lua
table.insert(tbl, 'val')
```

- `table.insert` - will append given value to the given table
- `tbl` - name of the table to add item to
- `'val'` - item to add to table

group: table

## Example: 
```lua
tbl = {1, 2}
table.insert(tbl, 3)
print(table.concat(tbl, ', '))
```
```
1, 2, 3

```

link_youtube: https://youtu.be/nmhXxDkFID0

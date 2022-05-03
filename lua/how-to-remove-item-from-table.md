# How to remove item from table

```lua
table.remove(tbl, 1)
```

- `table.remove` - will remove an element from given position
- `tbl` - name of the table to remove item from
- `1` - position to remove item from

group: table

## Example: 
```lua
tbl = {1, 2, 3}
table.remove(tbl, 2)
print(table.concat(tbl, ', '))
```
```
1, 3

```

link_youtube: https://youtu.be/IpMKGfyHl_w

# How to print table

```lua
for k, v in pairs(tbl) do print(k, v) end
```

- `for k, v in pairs(tbl)` - iterate through all items of `tbl` table
- `tbl` - table to print
- `print(k, v)` - print key and value of each table element

group: print_table

## Example: 
```lua
tbl = {a= 1, b= 2, c= 3}
for k, v in pairs(tbl) do print(k, v) end
```
```
c	3
b	2
a	1

```

link_youtube: https://youtu.be/mW2BUxzrJXU

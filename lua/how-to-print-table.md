# How to print table

```lua
print(table.concat(tbl, ', '))
```

- `table.concat` - join all given table items using given symbol
- `tbl` - table to print
- `', '` - string to join table items when printing

group: print_table

## Example: 
```lua
tbl = {1, 2, 3}
print(table.concat(tbl, ', '))
```
```
1, 2, 3

```


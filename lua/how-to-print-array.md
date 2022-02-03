# How to print array

```lua
print(table.concat(arr, ', '))
```

- `table.concat` - join all given array items using given symbol
- `arr` - array to print
- `', '` - string to join array items when printing

group: print_table

## Example: 
```lua
arr = {1, 2, 3}
print(table.concat(arr, ', '))
```
```
1, 2, 3

```


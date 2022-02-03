# How to append an element to array

```lua
table.insert(arr, 'val')
```

- `table.insert` - will append given value to the given array
- `arr` - array to append value to
- `'val'` - value to append to array

group: array_add

## Example: 
```lua
arr = {1, 2}
table.insert(arr, 3)
print(table.concat(arr, ', '))
```
```
1, 2, 3

```


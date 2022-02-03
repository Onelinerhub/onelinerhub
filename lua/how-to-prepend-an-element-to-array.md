# How to prepend an element to array

```lua
table.insert(arr, 1, 'val')
```

- `table.insert` - will append given value to the given array
- `arr` - array to append value to
- `'val'` - value to append to array
- `, 1` - will insert new value at the beginning (first element) of the array

group: array_add

## Example: 
```lua
arr = {2, 3}
table.insert(arr, 1, 1)
print(table.concat(arr, ', '))
```
```
1, 2, 3

```


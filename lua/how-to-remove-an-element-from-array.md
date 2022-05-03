# How to remove an element from array

```lua
table.remove(arr, 2)
```

- `table.remove` - will remove an element at given position
- `arr` - array to remove element from
- `2` - position to remove an element from

group: array_add

## Example: 
```lua
arr = {1, 2, 3}
table.remove(arr, 2)
print(table.concat(arr, ', '))
```
```
1, 3

```

link_youtube: https://youtu.be/FAb1DmFGMAE

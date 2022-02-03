# How to get random table item

```lua
math.randomseed(os.time())
el = tbl[math.random(1, #tbl)]
```

- `math.randomseed(os.time())` - init unique random generator (use local time for seed)
- `math.random(` - return random number within given range
- `tbl` - table to get random element from
- `1,` - min random value (first index of table)
- `#tbl` - max random value (table size)
- `el` - will contain random element from given table

group: random

## Example: 
```lua
math.randomseed(os.time())
tbl = {1, 2, 3}
el = tbl[math.random(1, #tbl)]
print(el)
```
```
3

```


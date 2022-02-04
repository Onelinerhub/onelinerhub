# Iterating in a "foreach" manner

```lua
tbl = {monday = 'work', sunday = 'family'}
for k,v in pairs(tbl) do
  print(k, v)
end
```

- `tbl` - sample table to iterate through
- `k,v` - `k` will get table item key and `v` - table item value
- `pairs(tbl)` - allows iterating using key/value pairs on specified table
- `print(k, v)` - do something with key/value of all table items

## Example: 
```lua
tbl = {monday = 'work', sunday = 'family'}
for k,v in pairs(tbl) do
  print(k, v)
end
```
```
sunday	family
monday	work

```


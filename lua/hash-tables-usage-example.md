# Hash tables usage example

```lua
tbl = {a=1, b=2}
tbl.c = 3
tbl.d = {sub: 'element'}
print(tbl.d.sub)
print(tbl.c)
```

- `tbl = {a=1, b=2}` - declare sample table with `a` and `b` keys
- `tbl.c = 3` - set value of `c` key to `3`
- `tbl.d` - set value of `d` key
- `{sub: 'element'}` - new table (will be stored in `d` key of sample table)
- `print(tbl.d.sub)` - prints value of `sub` key of `d` table of sample table
- `print(tbl.c)` - print value of `c` key of sample table

## Example: 
```lua
tbl = {a=1, b=2}
tbl.c = 3
tbl.d = {sub='element'}
print(tbl.d.sub)
print(tbl.c)
```
```
element
3

```


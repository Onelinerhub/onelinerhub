# Using switch...case

### Since there's no `switch` statement in Lua, we'll use `else/if`:

```lua
if      var == 1 then print('1')
elseif  var == 2 then print('2')
elseif  var == 3 then print('3')
elseif  var == 4 then print('4')
else                  print('other')
end
```

- `var` - variable to check values of
- `elseif` - we can use as many `elseif`s as we need

## Example: 
```lua
var = 3
if      var == 1 then print('1')
elseif  var == 2 then print('2')
elseif  var == 3 then print('3')
elseif  var == 4 then print('4')
else                  print('other')
end
```
```
3

```

link_youtube: https://youtu.be/qADemabPrX0

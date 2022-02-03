# How to create function

```lua
function say_hi(to)
   return 'Hi ' .. to.. '!';
end
```

- `function` - declare new function
- `say_hi` - function name
- `to` - argument(s)
- `return 'Hi ' .. to.. '!';` - implementation (returns greeting string in our case)
- `end` - ends function block

## Example: 
```lua
function say_hi(to)
   return 'Hi ' .. to .. '!';
end

print( say_hi('all') )
```
```
Hi all!

```


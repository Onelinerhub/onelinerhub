# How to create function

```lua
function say_hi(to)
   return 'Hi ' .. to.. '!';
end
```

- `function say_hi` - declare new function named `say_hi`
- `(to)` - argument(s)
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

link_youtube: https://youtu.be/N-oHU1-q8YY

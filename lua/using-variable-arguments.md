# Using variable arguments

```lua
function hi(...)
  local arg={...}
  for i,v in ipairs(arg) do
    print('Hi ' .. v .. '!')
  end
end

hi('Donald')
hi('Joe', 'Donald')
```

- `function hi` - declare sample function with variable arguments
- `local arg` - make `arg` variable contain list of function arguments
- `for i,v in ipairs(arg)` - iterate through all arguments
- `print('Hi ' .. v .. '!')` - sample code that prints argument value (access from `v` variable)

## Example: 
```lua
function hi (...)
  local arg={...}
  for i,v in ipairs(arg) do
    print('Hi ' .. v .. '!')
  end
end

hi('Donald')
hi('Joe', 'Donald')
```
```
Hi Donald!
Hi Joe!
Hi Donald!

```

link_youtube: https://youtu.be/38VvUsi4zmE

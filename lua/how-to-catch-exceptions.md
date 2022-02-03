# How to catch exceptions

### In order to handle errors, we need to encapsulate our code inside a function and then use `pcall()` to safely calls our function:

```lua
function test()
  error()
end
    
if not pcall(test) then
  print('error happened')
end
```

- `function test()` - sample function that will always return an error
- `error()` - raises error in Lua
- `if not pcall(test) then` - check if there were any errors
- `pcall` - calls given function safely and returns `true` if no error happened
- `print('error happened')` - prints this message if any errors happened inside `test()` function

group: exception

## Example: 
```lua
function test()
  error()
end
    
if not pcall(test) then
  print('error happened')
end
```
```
error happened

```


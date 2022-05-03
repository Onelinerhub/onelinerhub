# How to throw exception

### In order to raise error, use `error()` function:

```lua
function test()
  error()
end
```

- `function test()` - sample function that will always return an error
- `error()` - raises error in Lua

group: exception

## Example: 
```lua
function test()
  error()
end

test()
```
```
lua: (error object is a nil value)
stack traceback:
	[C]: in function 'error'
	/tmp/test.lua:2: in function 'test'
	/tmp/test.lua:5: in main chunk
	[C]: in ?
```

link_youtube: https://youtu.be/BAkveOaIDo4

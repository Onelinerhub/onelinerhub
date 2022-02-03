# How to break loop

### Lua doesn't have continue statement, but we can easily use `goto` instead:

```lua
while true do
  if ( true ) then break end
end
```

- `while true do` - sample loop
- `if ( true ) then` - condition to break loop execution (always break in our case)
- `break` - exists loop

group: loop

## Example: 
```lua
x = 0
while true do
  x = x+1
  if (x > 10) then break end
  print(x)
end
```
```
1
2
3
4
5
6
7
8
9
10

```


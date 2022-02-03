# How to break loop

```lua
while true do
  if ( true ) then break end
end
```

- `while true do` - sample loop
- `if ( true ) then` - condition to break loop on (always true in our case)
- `break` - will break loop execution

## Example: 
```lua
x = 1
while true do
  if (x > 10) then break end
  print(x)
  x = x+1
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


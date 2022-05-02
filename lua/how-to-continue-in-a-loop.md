# How to continue in a loop

```lua
while true do
  ::mark::
  -- do something
  if ( true ) then goto mark end
end
```

- `while true do` - sample loop
- `if ( true ) then` - condition to stop loop cycle and continue from the start
- `::mark::` - mark loop start to have a change to go here later
- `goto mark` - will continue execution at specified place inside loop

group: loop

## Example: 
```lua
x = 0
while true do
  ::start::
  x = x+1
  
  if (x < 5) then goto start end
  if (x > 10) then break end
  print(x)
end
```
```
5
6
7
8
9
10

```

link_youtube: https://youtu.be/j3bZQ9G3MWM

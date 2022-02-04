# Capturing groups from regex

```lua
local str = 'Hi, Donald! Do you like Joe?';
local n1, n2 = str:match('(D.+\\?)!.+(J.+)?')
```

- `local str` - sample string to capture regex groups from
- `match` - match given string with specified regex and returns captured groups values
- `n1, n2` - variables will get captured groups

group: regex

## Example: 
```lua
local str = 'Hi, Donald! Do you like Joe?';
local n1, n2 = str:match('(D.+\\?)!.+(J.+)?')
print(n1)
print(n2)
```
```
Donald
Joe

```


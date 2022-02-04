# Regex match and replace

```lua
local str = 'Hi, Donald! Do you like Joe?';
local str1 = str:gsub('D.+\\?!', 'Bill')
```

- `local str` - sample string to find and replace in based on regex
- `gsub` - will match and replace found strings based on regex
- `str1` - will contain final string

group: regex

## Example: 
```lua
local str = 'Hi, Donald! Do you like Joe?';
local str1 = str:gsub('D.+\\?!', 'Bill!')
print(str1)
```
```
Hi, Bill! Do you like Joe?

```


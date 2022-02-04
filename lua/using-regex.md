# Using regex

```lua
local str = 'Hi you all';
str:match('l+')
```

- `'Hi you all'` - sample string to match regex in
- `match` - match given string with specified regex
- `'l+'` - sample regex (will match all occurrences of `l` letter)

## Example: 
```lua
local str = 'Hi you all';
print(str:match('l+'))
```
```
ll

```


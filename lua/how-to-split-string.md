# How to split string

### Let's split a string by space:

```lua
str = "green yellow blue"
words = {}

for w in string.gmatch(str, "[^ ]+") do
   table.insert(words, w)
end
```

- `str` - sample string to split
- `words` - this array will container list of words
- `string.gmatch` - finds all matches by a given regex
- `for w in` - iterate through all matches items
- ` "[^ ]+"` - match all symbols except space (thus, we're going to split by space here)
- `table.insert(words, w)` - append found match (word) to `words` array

group: strings

## Example: 
```lua
str = "green yellow blue"
words = {}

for w in string.gmatch(str, "[^ ]+") do
   table.insert(words, w)
end

print(table.concat(words, ', '))
```
```
green, yellow, blue

```


# How to find substring in a string

```lua
start,stop = string.find("Hi all of you", "all")
```

- `string.find` - finds given substring in a given string
- `"Hi all of you"` - string to search in
- `"all"` - string to search for
- `start` - found substring start position
- `stop` - found substring end position

group: strings

## Example: 
```lua
start,stop = string.find("Hi all of you", "all")
print(start)
print(stop)
```
```
4
6

```


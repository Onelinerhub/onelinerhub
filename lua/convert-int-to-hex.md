# Convert int to hex

```lua
hex = string.format("%x", num)
```

- `num` - integer to convert to hex
- `string.format` - formats string with a given set of rules
- `"%x"` - present given integer in its hex form
- `hex` - will contain converted hex

group: convert_num

## Example: 
```lua
num = 123
hex = string.format("%x", num)
print(hex)
```
```
7b

```


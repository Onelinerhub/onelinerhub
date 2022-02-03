# How to format a string

```lua
formatted = string.format("this is %s and %s", var1, var2)
```

- `formatted` - will contain formatted string
- `string.format` - formats specified string
- `"this is %s and %s"` - string [format pattern](https://en.wikipedia.org/wiki/Printf_format_string) to use
- `var1, var2` - variables to embed

group: strings

## Example: 
```lua
formatted = string.format("Hi %s, it's %d year", 'all', os.date('%Y'))
print(formatted)
```
```
Hi all, it's 2022 year

```


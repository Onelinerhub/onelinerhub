# How to split string by length

```python
str = "somelongstring"
chunk = 3
list = [ str[i*chunk:i*chunk+chunk] for i in range(0, int(len(str)/chunk)) ]
```

- `str` - example string to split
- `chunk` - size of the substring to split by
- `list` - will contain list with resulting substrings
- `range(0, int(len(str)/chunk))` - iterate amount of chunks that can fit in our string
- `i*chunk:i*chunk+chunk` - select substring for current chunk

group: split_string

## Example: 
```python
str = "somelongstring"
chunk = 3
list = [ str[i*chunk:i*chunk+chunk] for i in range(0, int(len(str)/chunk)) ]
print(list)
```
```
['som', 'elo', 'ngs', 'tri']

```

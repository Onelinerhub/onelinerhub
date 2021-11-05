# How to find key in dict by value

```python
found_key = list(my_dict.keys())[list(my_dict.values()).index('needle')]
```

- `found_key` - key of the found value
- `my_dict` - dict to search key by value in
- `keys()` - returns list of dict keys
- `values()` - returns list of dict values
- `index(` - return index of found element in list
- `list(` - convert specified argument to list

group: find_element

## Example: 
```python
my_dict = {'first': 'a', 'second': 'b'}
found_key = list(my_dict.keys())[list(my_dict.values()).index('b')]
print(found_key)
```
```
second

```

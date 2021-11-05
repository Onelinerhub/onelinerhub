# How to delete element from dict

```python
del my_dict[key]
```

- `del` - removes element from dict by key
- `my_dict` - dict to remove element from
- `key` - key of the element to remove

group: delete_element

## Example: 
```python
my_dict = {'first': 'a', 'second': 'b', 'third': 'c'}
del my_dict['second']
print(my_dict)
```
```
{'first': 'a', 'third': 'c'}

```

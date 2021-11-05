# How to merge two dictionaries

```python
dict1 = {'first': 'a'}
dict2 = {'second': 'b'}

dict1.update(dict2)
```

- `dict1` - first dict to merge
- `dict2` - second dict to merge with first
- `update` - will merge with specified dict (`dict2` in our case)

group: merge_objects

## Example: 
```python
dict1 = {'first': 'a'}
dict2 = {'second': 'b'}

dict1.update(dict2)
print(dict1)
```
```
{'first': 'a', 'second': 'b'}

```

## Additional keywords
- join

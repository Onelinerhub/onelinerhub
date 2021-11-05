# How to order dict by keys

```python
sorted = dict(sorted(unsorted.items(), key=lambda item: item[0]))
```

- `unsorted` - source dict to sort
- `.items()` - returns list of dict key/value tuples
- `item[0]` - key to sort given list by (keys in our case)
- `dict(` - converts list of key/value tuples back into dict

group: order

## Example: 
```python
unsorted = {'second': 'b', 'first': 'a'}
sorted = dict(sorted(unsorted.items(), key=lambda item: item[0]))
print(sorted)
```
```
{'first': 'a', 'second': 'b'}

```

## Additional keywords
- sort

# How to order dict by values

```python
sorted = dict(sorted(unsorted.items(), key=lambda item: item[1]))
```

- `unsorted` - source dict to sort
- `.items()` - returns list of dict key/value tuples
- `item[1]` - key to sort given list by (values in our case)
- `dict(` - converts list of key/value tuples back into dict

group: order

## Example: 
```python
unsorted = {'first': 'b', 'second': 'a'}
sorted = dict(sorted(unsorted.items(), key=lambda item: item[1]))
print(sorted)
```
```
{'second': 'a', 'first': 'b'}

```

## Additional keywords
- sort

# Reverse a list using slicing

```python
list_a = ["foo", "bar", "baz"]
|{|list_reversed = list_a[::-1]|}|

print(list_reversed)
```

- \[::-1\] - slicing operator where the index is accessed as `[start:stop:step]`. If you define the `-1` step, the program will count the reverse index list(from the end to the beggining)


# Example
```python
list_a = ["foo", "bar", "baz"]
list_reversed = list_a[::-1]
print(list_reversed)
```
```bash
['baz', 'bar', 'foo']
```

group: reverse_list

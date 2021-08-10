# Reverse a list with slicing

```python
list_a = ["foo", "bar", "baz"]
list_reversed = list_a[::-1]

print(list_reversed)
```



- output: ['baz', 'bar', 'foo']
- this happens because of the slicing operator where the index is accessed as [start:stop:step] 
- if you define the step a -1, the program will count the reverse index list(from the end to the beggining)
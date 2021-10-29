# How to convert all list members to another data type

```python
converted = list(map(new_type, list_of_items))
```

- `converted` - new list that contain converted values
- `list(` - convert the final result to list
- `new_type` - data type you want the list member to convert to(target data type) e.g.(str, int, bool)
- `list_of_items` - list you want to source list
- `map(` - applies specified function to each element of specified list

## Example: 
```python
list_of_numbers = ["1", "2", "3"]
converted = list(map(int, list_of_numbers))
print(converted)
```
```
[1, 2, 3]

```

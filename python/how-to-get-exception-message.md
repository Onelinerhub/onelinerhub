# How to get exception message

```python
try:
  raise Exception('hi')
except Exception as mye:
  message = str(mye)
```

- `message` - will store exception message
- `str(` - convert exception to string (to get it's error message)
- `mye` - variable that stores exeption
- `raise Exception('hi')` - throws example exception

group: exception

## Example: 
```python
try:
  raise Exception('hi')
except Exception as e:
  print(e)
```
```
hi

```

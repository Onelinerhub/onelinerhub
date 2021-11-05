# How to get function arguments

```python
def my_func(x, y, z):
  args = locals()
```

- `my_func` - example function
- `locals()` - returns dict with local variables (to make sure it includes arguments only, have it on the first line of the function)

## Example: 
```python
def my_func(x, y, z):
  print(locals())
  
my_func(1, 2, 3)
```
```
{'x': 1, 'y': 2, 'z': 3}

```

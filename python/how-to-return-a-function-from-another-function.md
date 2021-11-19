# How to return a function from another function

```python
def some_func():

  def other_func():
    return 'hi'

  return other_func
```

- `some_func()` - this function to return another function
- `def other_func` - defines another function inside parent function (we will return this function)
- `return 'hi'` - example value returned from inner function
- `return other_func` - will return `other_func` function

## Example: 
```python
def some_func():

  def other_func():
    return 'hi'

  return other_func
  
f = some_func()
print(f())
```
```
hi

```

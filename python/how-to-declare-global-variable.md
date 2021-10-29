# How to declare global variable

```python
var = 1

def fnc():
  global var
  # do something with var

```

- `var` - declare variable to be used as global and assign value
- `global var` - declares `var` as global variable - now can be used in function

## Example: 
```python
var = 1

def fnc():
  global var
  var = 2
  
fnc()
print(var)

```
```
2

```

## Additional keywords
- define global variable

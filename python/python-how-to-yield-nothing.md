# How to yield nothing

```python
def yield_nothing():
  return
  yield
```

- `yield_nothing()` - name of the generator function to yield nothing
- `return` - returns nothing
- `yield` - yields after return (so never actually yields anything)

group: yield

## Example: 
```python
def yield_nothing():
  return
  yield

print('1')

for el in yield_nothing():
  print(el)
  
print('2')
```
```
1
2

```

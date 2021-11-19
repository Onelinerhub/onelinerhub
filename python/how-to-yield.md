# How to yield

```python
def squares():
  x = 0
  while x < 5:
    x = x + 1
    yield x*x
```

- `def squares()` - name of the generator function to yield something
- `while x < 5` - we'll yield some values until x is `5`
- `x = x + 1` - increment `x`
- `yield x*x` - yields square of `x`

group: yield

## Example: 
```python
def squares():
  x = 0
  while x < 5:
    x = x + 1
    yield x*x

print('A')

for el in squares():
  print(el)
  
print('B')
```
```
A
1
4
9
16
25
B

```

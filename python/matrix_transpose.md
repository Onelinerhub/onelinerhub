# How to find the transpose of a matrix
```python
mT = [[ row[col] for row in mO] for col in range( len(mO[0]) )]
```

- mT - will contain the new matrix
- mO - the old matrix


## Example
```python
m = [[ 2, 4 ] for n in range(3)]
print("M:\n" + str(m) + "\n")


mT = [[ row[col] for row in m] for col in range( len(m[0]) )]
print("Transpose of M:\n" + str(mT))
```
```bash
M:
[[2, 4], [2, 4], [2, 4]]

Transpose of M:
[[2, 2, 2], [4, 4, 4]]
```

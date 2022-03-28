# How to iterate Numpy array in loop

```python
import numpy as np
someArray = np.array([[1,2,3,4],[5,6,7,8]])
for number in someArray.flat: print(number)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `someArray.flat` - will return flat 1-dimensional array from given array
- `for number in` - iterate though all values of given array
- `print(number)` - sample loop body to process all iterated values

## Example: 
```python
import numpy as np
someArray = np.array([[1,2,3,4],[5,6,7,8]])
for number in someArray.flat: print(number)
```
```
1
2
3
4
5
6
7
8

```


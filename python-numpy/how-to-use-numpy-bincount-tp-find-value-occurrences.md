# How to use Numpy bincount tp find value occurrences

```python
import numpy as np

array = np.array([1,2,3,3,2,2,3])
counts = np.bincount(array)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.bincount` - count number of occurrences of each value in array of non-negative ints
- `array` - array to count values in
- `counts` - will contain final array with counted values

## Example: 
```python
import numpy as np

array = np.array([2,1,2,3,3,2,2,3])
print( np.bincount(array) )
```
```
[0 1 4 3]

```


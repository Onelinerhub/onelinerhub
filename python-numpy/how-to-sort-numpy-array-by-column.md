# How to sort Numpy array by column

```python
import numpy as np
a = np.array([[3, 1], [4, 2], [5, 7]])

sorted = np.sort(a.view('i8,i8'), order=['f0'], axis=0).view(np.int)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.sort` - sort specified array with specified parameters
- `a.view('i8,i8')` - creates a view of `a` array to make structured array of fields
- `order=['f0']` - will sort given structured array by first column (use `f1` for second column and so on)
- `axis=0` - sort array vertically
- `view(np.int)` - convert given view back to 2-dimensional array of integers

group: sort

## Example: 
```python
import numpy as np
a = np.array([[3, 1], [4, 2], [2, 7]])

print(a)

sorted = np.sort(a.view('i8,i8'), order=['f0'], axis=0).view(np.int)
print(sorted)
```
```
[[3 1]
 [4 2]
 [2 7]]
[[2 7]
 [3 1]
 [4 2]]

```


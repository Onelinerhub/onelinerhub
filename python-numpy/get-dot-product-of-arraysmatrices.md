# Get dot product of arrays/matrices

```python
import numpy as np 

a = np.array([[1,2],[3,4]]) 
b = np.array([[5,6],[7,8]]) 

prod = np.dot(a,b)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.dot(` - returns dot product of specified arrays
- `prod` - will contain resulting array/matrices

group: product

## Example: 
```python
import numpy as np 

a = np.array([[1,2],[3,4]]) 
b = np.array([[5,6],[7,8]]) 

print(np.dot(a,b))
```
```
[[19 22]
 [43 50]]

```


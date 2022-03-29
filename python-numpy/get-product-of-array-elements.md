# Get product of array elements

```python
import numpy as np 

a = np.array([1,2,3,4])

prod = np.dot(a,b)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.prod(` - returns product of elements of specified array
- `prod` - will contain resulting value

group: product

## Example: 
```python
import numpy as np 

a = np.array([1,2,3,4])

print(np.prod(a))
```
```
24

```


# Get product of array elements over specific axis

```python
import numpy as np 

a = np.array([[1,2], [3,4]])

prod_x = np.prod(a, axis=0)
prod_y = np.prod(a, axis=1)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `.prod(` - returns product of elements of specified array
- `axis=` - specify axis to calculate products over
- `prod_x` - will contain array or vertical products
- `prod_y` - will contain array of horizontal products

group: product

## Example: 
```python
import numpy as np 

a = np.array([[1,2], [3,4]])

prod_x = np.prod(a, axis=0)
prod_y = np.prod(a, axis=1)

print(a)
print(prod_x)
print(prod_y)
```
```
[[1 2]
 [3 4]]
[3 8]
[ 2 12]

```


# How to use multiple conditions in where()

```python
import numpy as np
array = np.arange(0, 100).reshape(10,10)

condition1 = array > 15
condition2 = array < 25

filtered = array[np.where(condition1 & condition2)]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.arange(` - generates array based on specified range
- `.reshape(` - changes shape of the array to the specified dimensions
- `condition1` - first condition to use
- `condition2` - second condition to use
- `condition1 & condition2` - use both conditions in `where` method
- `where(` - returns filtered elements from array based on condition

group: where

## Example: 
```python
import numpy as np

array = np.arange(0, 100).reshape(10,10)
condition1 = array > 15
condition2 = array < 25

print(array[np.where(condition1 & condition2)])
```
```
[16 17 18 19 20 21 22 23 24]

```


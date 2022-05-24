# How to fill Numpy array with values

```python
import numpy as np

array = np.empty(10)
array.fill(5)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.empty` - generate empty Numpy array of the specified shape
- `10` - we're creating empty array of 10 elements
- `.fill` - fill array with specified value
- `5` - we're going to fill our array with values of `5`

## Example: 
```python
import numpy as np

array = np.empty(10)
array.fill(5)

print(array)
```
```
[5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

```


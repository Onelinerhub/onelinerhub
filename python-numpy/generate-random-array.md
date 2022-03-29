# Generate random array

```python
import numpy as np
arr = np.random.rand(3,2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.random.rand(` - returns array of random float values in `0...1` range of a given size
- `(3,2)` - size of the array to generate (`3x2` in our case)
- `arr` - generated aarray

group: random

## Example: 
```python
import numpy as np
arr = np.random.rand(3,2)
print(arr)
```
```
[[2.67415065e-02 5.37803132e-04]
 [4.49957894e-01 4.14168312e-01]
 [5.26813058e-01 8.14829319e-01]]

```


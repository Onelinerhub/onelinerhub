# Generate random array with normal distribution

```python
import numpy as np
arr = np.random.randn(3, 2)
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.random.randn(` - returns array of random float values with normal distribution
- `(3, 2)` - array size to generate (`3x2` in our case)
- `arr` - generated array

group: random

## Example: 
```python
import numpy as np
arr = np.random.randn(3, 2)
print(arr)
```
```
[[-0.27814326 -1.28738251]
 [ 0.46370535 -0.29249692]
 [ 0.65619653 -0.63973934]]

```


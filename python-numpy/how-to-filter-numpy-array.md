# How to filter Numpy array

```python
import numpy as np

array = np.array([1,2,3,4,5])
filtered = array[array >= 3]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `array >= 3` - condition to filter upon (selects all array values bigger or equal to `3`)
- `array[array >= 3]` - filteres `array` based on condition expression
- `filtered` - will contain filtered array

## Example: 
```python
import numpy as np

array = np.array([1,2,3,4,5])
filtered = array[array >= 3]

print(filtered)
```
```
[3 4 5]

```

link_youtube: https://youtu.be/Xrx7DLhy0Uc

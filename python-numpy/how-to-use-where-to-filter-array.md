# How to use where() to filter array

```python
import numpy as np

array = np.arange(0, 100).reshape(10,10)

filtered = array[np.where(array > 80)]
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.arange(` - generates array based on specified range
- `.reshape(` - changes shape of the array to the specified dimensions
- `where(` - returns filtered elements from array based on condition
- `array > 80` - sample condition (choose only elements which value is more than `80`)

group: where

## Example: 
```python
import numpy as np

array = np.arange(0, 100).reshape(10,10)

print(array[np.where(array > 80)])
```
```
[81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]

```


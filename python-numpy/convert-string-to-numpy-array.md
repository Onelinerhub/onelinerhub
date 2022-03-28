# Convert string to Numpy array

```python
import numpy as np

str = '1, 2, 3, 4'
a = np.fromstring(str, dtype=int, sep=',')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `'1, 2, 3, 4'` - sample
- `.fromstring(` - load Nunpy array data from given string and rules
- `dtype=int` - elements type from [Numpy types](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types) to use when parsing string
- `sep=','` - elements separator to use when parsing string

group: string

## Example: 
```python
import numpy as np

str = '1, 2, 3, 4'
a = np.fromstring(str, dtype=int, sep=',')

print(type(a))
print(a)
```
```
<class 'numpy.ndarray'>
[1 2 3 4]

```


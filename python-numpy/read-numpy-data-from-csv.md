# Read Numpy data from CSV

```python
import numpy as np
a = np.genfromtxt('/var/www/examples/column.csv')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.genfromtxt(` - loads Numpy array data from given `CSV` file
- `/var/www/examples/column.csv` - file path to load data from

group: csv

## Example: 
```python
import numpy as np
a = np.genfromtxt('/var/www/examples/column.csv')
print(a)
```
```
[1. 2. 3. 4. 5. 6. 7. 8. 9.]

```


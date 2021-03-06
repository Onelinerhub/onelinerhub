# How to load Numpy matrix from CSV file

```python
import numpy as np

db = np.loadtxt('/tmp/db.csv', delimiter=',')
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.loadtxt` - load array from `csv` file
- `/tmp/db.csv` - path to text `csv` that was previously saved with [savetxt()](/python-numpy/how-to-save-numpy-matrix-to-csv-file)
- `db` - will contain loaded data

group: csv

## Example: 
```python
import numpy as np

db = np.loadtxt('/tmp/db.csv', delimiter=',')
print(db)
```
```
[[1. 2.]
 [3. 4.]
 [5. 6.]]

```


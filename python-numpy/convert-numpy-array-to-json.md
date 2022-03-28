# Convert Numpy array to JSON

```python
import numpy as np
import json as json

a = np.array([[1, 2], [3, 4], [5, 6]])

jsn = json.dumps(a.tolist())
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `import json as json` - load JSON module to encode to JSON
- `np.array` - declare Numpy array
- `[[1, 2], [3, 4], [5, 6]]` - sample multi-dimensional array
- `.tolist()` - convert given Numpy array to list
- `json.dumps` - convert given list to JSON

group: json

## Example: 
```python
import numpy as np
import json as json

a = np.array([[1, 2], [3, 4], [5, 6]])

jsn = json.dumps(a.tolist())
print(jsn)
```
```
[[1, 2], [3, 4], [5, 6]]

```


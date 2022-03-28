# Load Numpy array data from JSON

```python
import numpy as np
import json as json

jsn = '[[1,2],[3,4]]'
a = np.array(json.loads(jsn))
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `import json as json` - load JSON module to parse JSON
- `np.array` - create Numpy array from given list
- `'[[1,2],[3,4]]'` - sample JSON string to create Numpy array from
- `json.loads(` - parse given JSON data to list

group: json

## Example: 
```python
import numpy as np
import json as json

jsn = '[[1,2],[3,4]]'
a = np.array(json.loads(jsn))
print(a)
```
```
[[1 2]
 [3 4]]

```


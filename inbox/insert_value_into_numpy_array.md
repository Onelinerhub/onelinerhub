# How to insert value into Numpy array

```python
import numpy as np
a = np.array([1, 2, 3])

np.insert(a, 3, 4) # insert single value at index 3
np.insert(a, 3, [4, 5]) # insert multiple values at index 3
np.insert(a, [1, 2], 4) # insert value at multiple positions
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `np.array` - declare Numpy array
- `np.insert` - insert value at specified index, where second argument is the index; can also insert value into multiple positions by specifying a list of indices
- also see `np.append` to add elements to end of an array 

## Example

```python
import numpy as np
a = np.array([1, 2, 3])

print(np.insert(a, 3, 4)) 
print(np.insert(a, 3, [4, 5])) 
print(np.insert(a, [1, 2], 4)) 
```
```
[1 2 3 4]
[1 2 3 4 5]
[1 4, 2, 4, 3]
```

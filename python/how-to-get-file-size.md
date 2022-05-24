# How to get file size

```python
import os
size = os.path.getsize('/path/to/file')
```

- `import os` - we need this module to set or get environment variables
- `path.getsize` - return size of the file in bytes by path
- `/path/to/file` - path to file to get size of

## Example: 
```python
import os

print(os.path.getsize('/tmp/numpy.npy'))
```
```
152

```


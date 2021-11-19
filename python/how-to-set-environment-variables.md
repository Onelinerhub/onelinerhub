# How to set environment variables

```python
import os
os.environ['SOMEVAR'] = 'someval'
```

- `import os` - we need this module to set or get environment variables
- `SOMEVAR` - name of the environment variable to set
- `someval` - value to assign

group: env

## Example: 
```python
import os
os.environ['SOMEVAR'] = 'someval'
print(os.environ['SOMEVAR'])
```
```
someval

```

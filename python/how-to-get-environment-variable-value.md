# How to get environment variable value

```python
import os
user = os.environ['USER']
```

- `import os` - we need this module to set or get environment variables
- `user` - will contain value of environment variable
- `os.environ['USER']` - get `USER` environment variable

group: env

## Example: 
```python
import os
user = os.environ['USER']
print(user)
```
```
www-data

```

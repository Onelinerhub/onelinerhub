# How to list files in current directory

```python
import os
filenames = os.listdir()
print(filenames)
```

- os - module which provides functions for interacting with the operating system
- os.listdir - returns the list of string as file names of the working directory (where python is currently running)

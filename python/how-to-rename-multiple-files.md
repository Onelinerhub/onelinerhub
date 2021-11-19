# Rename Multiple Files

```python
import os

for file in os.listdir('/dir'):
    os.rename(file, f"/dir/new_{file}")
```

- import os - library to work with files and dirs
- `os.listdir(` - gets all the files inside specified directory, iterates each file inside the loop
- '/dir' - directory with files to rename
- `new_` -  prefix to add to renamed files
- `rename(` - function to rename the file

group: rename_file

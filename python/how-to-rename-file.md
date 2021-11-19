# How to rename a file

```python
import os

old_file_name = "python.txt"
new_file_name = "python_renamed.txt"

os.rename(old_file_name, new_file_name)
```

- import os - library to work with files and dirs
- `old_file_name` - source file name that needs to be renamed
- `new_file_name` - new name of the file
- `os.rename(` - renames source file (first argument) to new name (second argument)

group: rename_file

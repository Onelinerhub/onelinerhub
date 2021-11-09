# How to rename file

### Rename A File
```python
import os

old_file_name = "python.txt"
new_file_name = "python_renamed.txt"

os.rename(old_file_name, new_file_name)
```

- `old_file_name` - the source file name that needs to be renamed.
- `new_file_name` -  the destination file name which is the new name of the file or directory
- `rename()` - function to rename the file

### Rename Multiple Files
```python
import os

for file in os.listdir("C:/Projects/Tryouts"):
    os.rename(file, f"C:/Projects/Tryouts/old_{file}")
```

- `old_file_name` - the source file name that needs to be renamed.
- `new_file_name` -  the destination file name which is the new name of the file or directory
- `rename()` - function to rename the file
- `os.listdir()` - method in a loop that can get all the files, iterates each file inside the loop

# How to list files in folder

```python
from os import listdir, path

dir = '/var/www/onelinerhub'
files = [f for f in listdir(dir) if path.isfile(path.join(dir, f))]
```

- `listdir, path` - import functions to work with directories and file pathes
- `dir =` - example dir to list files in
- `files =` - resulting list which will contains files
- `listdir(` - lists all files and folders inside specified directory
- `if path.isfile` - checks if given path is a file
- `path.join(dir, f)` - returns full file path from directory and file name

group: list_files

## Example: 
```python
from os import listdir, path

dir = '/var/www/onelinerhub'
files = [f for f in listdir(dir) if path.isfile(path.join(dir, f))]
print(files)
```
```
['template_simple.md', 'LICENSE', 'README.md', 'example.png', 'template.md']

```

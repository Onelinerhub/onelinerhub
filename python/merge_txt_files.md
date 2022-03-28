# Combine multiple txt files into one

### We'll read all files in a certain directory and merge them into single `output.txt` file:

```python
import os
path = '/path/to/files'
list = []
outputcontent = ''

for (root, dirs, file) in os.walk(path):
  for f in file:
    if '.txt' in f:
      filecontent = open(path + f, mode="r")
      filecontent = filecontent.read()
      outputcontent += filecontent + "\n"

with open('output.txt', mode='a') as f:
  f.write(outputcontent)
```

- `import os` - we need this module to get list of files in a directory
- `/path/to/files` - path to a directory with text files to merge
- `os.walk(path)` - iterate through all files in specified directory
- `if '.txt' in f` - work with `txt` files only
- `filecontent` - reads all content from file
- `f.write(outputcontent)` - write resulting content into `output.txt`

group: combine_files



# Combine multiple txt files into one

### We'll read all files in a certain directory and merge them into single `output.txt` file:

```python
import os
path = '/path/to/files'
list = []
outputcontent = ''

with open('output.txt', mode='a') as fw:
  for (root, dirs, file) in os.walk(path):
    for f in file:
      if '.txt' in f:
    	  with open(path + f, mode="r") as filecontent:
    	    filecontent = filecontent.read()
    	    fw.write(filecontent + "\n")
	      
```

- `import os` - we need this module to get list of files in a directory
- `/path/to/files` - path to a directory with text files to merge
- `os.walk(path)` - iterate through all files in specified directory
- `if '.txt' in f` - work with `txt` files only
- `filecontent.read()` - reads all content from file
- `fw.write(filecontent` - write each file content into `output.txt`

group: combine_files



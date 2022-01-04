# Combine multiple .txt files into one
```python
import os
path="../data/"
list = []
outputcontent = ""

for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.txt' in f:
        	filecontent = open(path + f, mode="r")
        	filecontent = filecontent.read()
        	# print(filecontent)

        	outputcontent += filecontent.replace("\n", "") + "\n"

with open('output.txt', mode="a") as f:
	f.write(outputcontent)
```

merge all .txt files in one directory to one file
# How to iterate through each line of a file

```bash
while IFS="" read -r p || [ -n "$p" ]; do echo $p; done < file.txt
```

- file.txt - text file we're going to read
- echo $p; - print line by line (replace this with your code)

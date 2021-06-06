# How to store each line of a file as an index of a list

```python
file_lines = [line.strip() for line in open("filename.txt")]
```

- file_lines - is a list of lines in the given file
- line.strip() - remove whitespace from both sides of the string
- filename.txt - file to read lines from

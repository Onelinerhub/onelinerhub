# How to read text file

```python
with open('/tmp/file.txt', 'r') as f:
  data = file.read()
```

- with open( - opens file with the specified mode
- /tmp/file.txt - path to the file we want to read
- 'r' - read mode
- read() - read all text from a file into a string

## Example
```python
with open('hello.txt', 'r') as f:
  data = file.read()
  print(data)
```
```
some text
```

# How to read text file

```python
with open('hello.txt', 'r') as f:
  data = file.read()
```

- open() - opens file with the specified mode
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

# How to read file

```bash
f = open('demofile.txt', 'r')
print(f.read())
```

- `'demofile.txt'` - name of the file to read
- `'r'` - used so that we can read file
- `f.read` - method for reading the content of the file


## Example 1: 
```python
f = open('demofile.txt', 'r')
print(f.read(5))
```
- `5` - return the 5 first characters of the file


## Example 2: 
```python
f = open('demofile.txt', 'r')
print(f.readline())
```
- `f.readline` - read one line of the file




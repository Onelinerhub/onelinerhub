# How to write list to file

```python
lst = ["abc", "def", "ghi"]
f = open("demofile.txt", "w")
for element in lst:
    f.write(element + "\n")
f.close()
```

- `'demofile.txt'` - name of the file to read
- `'w'` - used so that we can write something into new file
- `f.write` - writes specified text into file
- `element` - items of list


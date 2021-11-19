# How to write list to file

```python
lst = ["abc", "def", "ghi"]
with open('out.txt', "w") as f:
    for element in lst:
        f.write(element + "\n")
```

- lst = - sample list to write to file
- `'out.txt'` - name of the file to read
- `'w'` - used so that we can write something into new file
- `f.write` - writes specified text into file
-  + "\n" - add new file after each element of the list
- `element` - item of list

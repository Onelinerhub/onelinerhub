# How to slugify string for filename or url path

Note: change string with your string or variable name
```python
slugified = "".join(x for x in string if x.isalnum())
```

- slugified - contain slugified string
- string - string that should slugify
- x - is one character of the given string each time
- isalnuum - is function that return True if the char is alphabet or numeric

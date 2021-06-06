# How to slugify string for filename or url path

Note: change string with your string or variable name
```python
slugified_string = "".join(x for x in string if x.isalnum())
```

- slugified_string - contain slugified string
- string - string that should slugify
- x - is one character of the given string each time
- x.isalnuum() - return True if the char is alphabet or numeric

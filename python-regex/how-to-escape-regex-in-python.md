# How to escape regex in Python?
// plain

To escape regex in Python, you can use the `re.escape()` function. This function takes a string as an argument and returns a string with all non-alphanumeric characters escaped.

For example:
```
import re

string = 'This is a string with *special* characters'

escaped_string = re.escape(string)

print(escaped_string)
```

## Output example

```
This\ is\ a\ string\ with\ \*special\*\ characters
```

The `re.escape()` function:
- takes a string as an argument
- returns a string with all non-alphanumeric characters escaped

## Helpful links
- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to escape regex in Python?](https://onelinerhub.com/python-regex/how-to-escape-regex-in-python)
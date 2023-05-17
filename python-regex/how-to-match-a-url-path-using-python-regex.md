# How to match a URL path using Python regex?
// plain

Python regex can be used to match a URL path. The `re` module provides a `re.match()` function which takes a regular expression pattern and a string and attempts to match the pattern to the string.

```
import re

url = 'https://www.example.com/path/to/file'

match = re.match('^https?://www\.example\.com/path/to/file$', url)

if match:
    print('Match found!')
else:
    print('No match found!')
```

## Output example

```
Match found!
```

## Code explanation

- `import re`: imports the `re` module which provides functions for working with regular expressions
- `re.match()`: takes a regular expression pattern and a string and attempts to match the pattern to the string
- `^`: matches the beginning of the string
- `$`: matches the end of the string

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

onelinerhub: [How to match a URL path using Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-url-path-using-python-regex)
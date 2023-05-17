# How to ignore case in Python regex?
// plain

To ignore case in Python regex, use the `re.IGNORECASE` flag. This flag can be passed as a second argument to `re.compile()` or `re.search()` functions.

## Example code

```
import re

pattern = re.compile('hello', re.IGNORECASE)

if pattern.search('Hello World'):
    print('Match found')
```

## Output example

```
Match found
```

## Code explanation

- `re.IGNORECASE`: flag to ignore case in Python regex
- `re.compile()`: function to compile a regex pattern
- `re.search()`: function to search for a regex pattern

## Helpful links
- [Python Regular Expression](https://docs.python.org/3/library/re.html)

onelinerhub: [How to ignore case in Python regex?](https://onelinerhub.com/python-regex/how-to-ignore-case-in-python-regex)
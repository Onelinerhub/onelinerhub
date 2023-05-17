# How to match a year with Python Regex?
// plain

Python Regex can be used to match a year with the following steps:

1. Create a regular expression pattern to match a year using the `re` module:
```
import re
year_pattern = re.compile(r'\d{4}')
```

2. Use the `findall()` method to search for the pattern in a string:
```
year_matches = year_pattern.findall('The year is 2020')
```

3. The `findall()` method will return a list of matches:
```
print(year_matches)
```

```
['2020']
```

## Code explanation

- `re` module: used to create regular expression patterns
- `compile()` method: used to compile a regular expression pattern
- `findall()` method: used to search for the pattern in a string

## Helpful links
- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to match a year with Python Regex?](https://onelinerhub.com/python-regex/how-to-match-a-year-with-python-regex)
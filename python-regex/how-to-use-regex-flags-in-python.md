# How to use regex flags in Python?
// plain

Regex flags are used to modify the behavior of a regular expression search in Python. Flags can be specified in the `re.compile()` function using the `re.IGNORECASE` or `re.I` flag to ignore case when matching strings.

## Example code

```
import re

pattern = re.compile(r'\w+', re.I)

string = 'Hello World'

match = pattern.search(string)

print(match.group())
```

## Output example

```
Hello
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.compile()` function.
- `pattern = re.compile(r'\w+', re.I)`: creates a regular expression pattern object using the `re.compile()` function and the `re.I` flag to ignore case when matching strings.
- `string = 'Hello World'`: creates a string to search.
- `match = pattern.search(string)`: searches the string for a match using the pattern object.
- `print(match.group())`: prints the matched string.

## Helpful links
- [Python Regular Expression Flags](https://www.programiz.com/python-programming/regex#flags)
- [Python re Module](https://docs.python.org/3/library/re.html)

onelinerhub: [How to use regex flags in Python?](https://onelinerhub.com/python-regex/how-to-use-regex-flags-in-python)
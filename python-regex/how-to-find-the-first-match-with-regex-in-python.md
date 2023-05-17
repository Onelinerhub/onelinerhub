# How to find the first match with regex in Python?
// plain

The `re` module in Python provides a `re.search()` function to find the first match of a pattern in a string.

## Example code

```
import re

string = 'The quick brown fox jumps over the lazy dog.'

match = re.search(r'quick', string)

if match:
    print('Found match:', match.group())
```

## Output example

```
Found match: quick
```

## Code explanation

- `import re`: imports the `re` module which provides the `re.search()` function
- `string = 'The quick brown fox jumps over the lazy dog.'`: defines the string to search
- `match = re.search(r'quick', string)`: searches for the pattern `quick` in the string
- `if match:`: checks if a match was found
- `print('Found match:', match.group())`: prints the found match

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)

onelinerhub: [How to find the first match with regex in Python?](https://onelinerhub.com/python-regex/how-to-find-the-first-match-with-regex-in-python)
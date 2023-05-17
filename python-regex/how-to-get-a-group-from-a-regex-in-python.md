# How to get a group from a regex in Python?
// plain

To get a group from a regex in Python, you can use the `re.search()` method. This method takes a regular expression pattern and a string and searches for that pattern within the string. If the pattern is found, it returns a `Match` object. The `Match` object has a `group()` method which returns the string matched by the regular expression.

## Example code

```
import re

string = 'The quick brown fox jumps over the lazy dog.'
pattern = r'(quick|lazy)'

match = re.search(pattern, string)
if match:
    print(match.group())
```

## Output example

```
quick
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.search()` method.
- `string = 'The quick brown fox jumps over the lazy dog.'`: creates a string to search for the pattern.
- `pattern = r'(quick|lazy)'`: creates a regular expression pattern to search for.
- `match = re.search(pattern, string)`: searches for the pattern within the string and returns a `Match` object if found.
- `if match:`: checks if a `Match` object was returned.
- `print(match.group())`: prints the string matched by the regular expression.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python re.search() Method](https://www.tutorialspoint.com/python/re_search.htm)

onelinerhub: [How to get a group from a regex in Python?](https://onelinerhub.com/python-regex/how-to-get-a-group-from-a-regex-in-python)
# How to match all letters with Python regex?
// plain

Python regex can be used to match all letters in a string. The `re` module provides a set of functions that allows us to search a string for a match.

```python
import re

# Match all letters
pattern = re.compile(r'[a-zA-Z]')

# Sample string
string = 'Hello World!'

# Find all matches
matches = pattern.findall(string)

# Print matches
print(matches)
```

## Output example

```
['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
```

The code above uses the `re.compile()` function to create a regular expression object. The `[a-zA-Z]` part of the expression is used to match all letters in the string. The `findall()` method is then used to find all matches in the string. Finally, the `print()` function is used to print out the matches.

Parts of the code:

- `import re`: imports the `re` module which provides functions for working with regular expressions.
- `pattern = re.compile(r'[a-zA-Z]')`: creates a regular expression object that matches all letters.
- `string = 'Hello World!'`: creates a sample string.
- `matches = pattern.findall(string)`: finds all matches in the string.
- `print(matches)`: prints out the matches.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match all letters with Python regex?](https://onelinerhub.com/python-regex/how-to-match-all-letters-with-python-regex)
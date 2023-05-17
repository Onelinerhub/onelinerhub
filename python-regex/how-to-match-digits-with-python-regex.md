# How to match digits with Python regex?
// plain

Python regex can be used to match digits with the `\d` character class. This character class matches any single digit from 0 to 9.

For example:
```
import re

string = '12345'

match = re.search(r'\d', string)

if match:
    print(match.group())
```

## Output example

```
1
```

The code above uses the `re.search()` function to search for a single digit in the string `12345`. The `\d` character class is used as the pattern to match. The `match.group()` function is then used to print the first digit that is matched.

## Code explanation

- `import re`: imports the `re` module which contains the functions needed for regex operations
- `string = '12345'`: assigns the string `12345` to the variable `string`
- `re.search(r'\d', string)`: searches for a single digit in the string `12345` using the `\d` character class as the pattern
- `match.group()`: prints the first digit that is matched

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match digits with Python regex?](https://onelinerhub.com/python-regex/how-to-match-digits-with-python-regex)
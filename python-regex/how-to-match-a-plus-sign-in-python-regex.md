# How to match a plus sign in Python regex?
// plain

To match a plus sign in Python regex, use the `+` character. This character will match one or more of the preceding character. For example, the following code will match any string that contains one or more `a` characters:

```python
import re

pattern = re.compile(r'a+')

string = 'aaabbbccc'

match = pattern.search(string)

if match:
    print(match.group())
```

## Output example

```
aaa
```

The code consists of the following parts:

1. `import re` - imports the `re` module which provides regular expression matching operations.
2. `pattern = re.compile(r'a+')` - creates a regular expression pattern object with the pattern `a+` which will match one or more `a` characters.
3. `string = 'aaabbbccc'` - creates a string to match against.
4. `match = pattern.search(string)` - searches the string for a match against the pattern.
5. `if match:` - checks if a match was found.
6. `print(match.group())` - prints the matched string.

## Helpful links

- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match a plus sign in Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-plus-sign-in-python-regex)
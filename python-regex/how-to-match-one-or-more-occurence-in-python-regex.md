# How to match one or more occurence in Python regex?
// plain

To match one or more occurence in Python regex, the `+` operator can be used. This operator matches one or more occurences of the preceding character or group.

For example,
```
import re

string = "Hello World"

# Match one or more occurences of 'l'
match = re.search(r'l+', string)

if match:
    print(match.group())
```

## Output example

```
ll
```

The code above uses the `re.search()` function to search for one or more occurences of the character `l` in the string `Hello World`. The `+` operator is used to match one or more occurences of `l`. The `match.group()` function is then used to print the matched occurences.

Parts of the code:
- `import re`: imports the `re` module which provides regular expression matching operations
- `re.search(r'l+', string)`: searches for one or more occurences of the character `l` in the string `string`
- `match.group()`: prints the matched occurences

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Regex Cheat Sheet](https://www.pybloggers.com/2018/08/python-regex-cheat-sheet/)

onelinerhub: [How to match one or more occurence in Python regex?](https://onelinerhub.com/python-regex/how-to-match-one-or-more-occurence-in-python-regex)
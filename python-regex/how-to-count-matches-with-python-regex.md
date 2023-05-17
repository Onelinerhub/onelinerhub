# How to count matches with Python regex?
// plain

Python regex can be used to count matches in a string. To do this, the `re.findall()` function can be used. This function returns a list of all matches in the string.

## Example code

```
import re

string = "This is a string with some words"

matches = re.findall(r"\w+", string)

print(matches)
```

## Output example

```
['This', 'is', 'a', 'string', 'with', 'some', 'words']
```

## Code explanation

- `import re`: imports the `re` module which contains the `findall()` function
- `re.findall(r"\w+", string)`: uses the `findall()` function to find all matches of the regex pattern `\w+` in the string
- `print(matches)`: prints the list of matches

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to count matches with Python regex?](https://onelinerhub.com/python-regex/how-to-count-matches-with-python-regex)
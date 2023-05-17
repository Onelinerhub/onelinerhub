# How to match whitespace in Python regex?
// plain

To match whitespace in Python regex, use the `\s` character class. This character class matches any whitespace character, including spaces, tabs, and line breaks.

## Example code

```
import re

text = "This is a test string"

pattern = re.compile(r"\s")

matches = pattern.finditer(text)

for match in matches:
    print(match)
```

## Output example

```
<re.Match object; span=(4, 5), match=' '>
<re.Match object; span=(9, 10), match=' '>
```

## Code explanation

- `import re`: imports the `re` module, which contains the functions needed to work with regular expressions
- `text = "This is a test string"`: creates a string to use for testing
- `pattern = re.compile(r"\s")`: creates a regular expression pattern that matches any whitespace character
- `matches = pattern.finditer(text)`: finds all matches of the pattern in the text
- `for match in matches:`: iterates over all matches
- `print(match)`: prints out each match

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match whitespace in Python regex?](https://onelinerhub.com/python-regex/how-to-match-whitespace-in-python-regex)
# How to match the end of a line with regex in Python?
// plain

The `$` character in a regular expression matches the end of a line. To match the end of a line with regex in Python, use the `re.search()` function with the `$` character in the regex pattern.

## Example code

```
import re

line = "This is the end of the line"

if re.search("end$", line):
    print("Match found")
```

## Output example

```
Match found
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.search()` function.
- `line = "This is the end of the line"`: assigns the string to the `line` variable.
- `if re.search("end$", line):`: checks if the `line` variable contains the `end` string at the end of the line using the `re.search()` function.
- `print("Match found")`: prints the `Match found` string if the `end` string is found at the end of the line.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

onelinerhub: [How to match the end of a line with regex in Python?](https://onelinerhub.com/python-regex/how-to-match-the-end-of-a-line-with-regex-in-python)
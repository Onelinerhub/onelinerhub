# How to match the beginning of a line with Python regex?
// plain

To match the beginning of a line with Python regex, the `^` character is used. This character is known as the "start of line" anchor.

## Example code

```
import re

line = "This is a line of text"

# Match the beginning of the line
match = re.search("^This", line)

if match:
  print("Match found!")
else:
  print("No match found!")
```

## Output example

```
Match found!
```

## Code explanation

- `import re`: imports the Python regex module
- `line = "This is a line of text"`: creates a string variable
- `match = re.search("^This", line)`: searches for the pattern `^This` in the string `line`
- `if match:`: checks if a match was found
- `print("Match found!")`: prints the message if a match was found
- `print("No match found!")`: prints the message if no match was found

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to match the beginning of a line with Python regex?](https://onelinerhub.com/python-regex/how-to-match-the-beginning-of-a-line-with-python-regex)
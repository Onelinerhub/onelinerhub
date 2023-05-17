# How to use backslash in Python regex?
// plain

Using backslash in Python regex is a way to escape special characters. For example, if you want to match a literal backslash, you need to use two backslashes in the regex.

```
import re

pattern = r"\\"

if re.search(pattern, "This is a backslash: \\"):
    print("Match!")
else:
    print("No match!")
```

## Output example

```
Match!
```

## Code explanation

- `import re`: imports the `re` module which provides regular expression matching operations
- `pattern = r"\\"`: creates a regular expression pattern object with a literal backslash
- `if re.search(pattern, "This is a backslash: \\"):`: searches for the pattern in the given string
- `print("Match!")`: prints "Match!" if the pattern is found
- `print("No match!")`: prints "No match!" if the pattern is not found

## Helpful links
- [Python Regular Expression Quick Guide](https://www.rexegg.com/regex-quickstart.html)
- [Python Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to use backslash in Python regex?](https://onelinerhub.com/python-regex/how-to-use-backslash-in-python-regex)
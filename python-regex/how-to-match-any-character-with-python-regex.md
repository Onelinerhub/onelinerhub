# How to match any character with Python regex?
// plain

The Python `re` module provides a set of functions that allows us to match any character using regular expressions. To match any character, we can use the `.` (dot) character. The `.` character matches any single character except for a newline.

## Example code

```
import re

pattern = r".*"

string = "Hello World!"

match = re.search(pattern, string)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
```

## Output example

```
Match found: Hello World!
```

## Code explanation


1. `import re`: This imports the `re` module which provides functions for working with regular expressions.
2. `pattern = r".*"`: This creates a regular expression pattern that matches any character. The `.` character matches any single character except for a newline. The `*` character matches the preceding character 0 or more times.
3. `string = "Hello World!"`: This creates a string that we will use to search for a match.
4. `match = re.search(pattern, string)`: This searches the `string` for a match using the `pattern`.
5. `if match:`: This checks if a match was found.
6. `print("Match found:", match.group())`: This prints the matched string.

## Helpful links

- [Python Regular Expression Quick Guide](https://www.tutorialspoint.com/python/python_reg_expressions.htm)
- [Python re Module](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match any character with Python regex?](https://onelinerhub.com/python-regex/how-to-match-any-character-with-python-regex)
# How to match a question mark in Python regex?
// plain

To match a question mark in Python regex, use the `?` character. This character is used to indicate that the preceding character is optional. For example, the following code will match strings that contain either one or two question marks:

```
import re

pattern = r"\?\??"

test_string = "This string contains one question mark?"

match = re.search(pattern, test_string)

if match:
    print("Match found!")
else:
    print("No match found!")
```

## Output example

```
Match found!
```

The code consists of the following parts:

- `import re`: This imports the `re` module, which provides functions for working with regular expressions.
- `pattern = r"\?\??"`: This defines the regular expression pattern. The `r` prefix indicates that the string is a raw string, which means that backslashes are not treated as escape characters. The `?` character is used to indicate that the preceding character is optional. In this case, the pattern will match strings that contain either one or two question marks.
- `test_string = "This string contains one question mark?"`: This defines the string that will be tested against the regular expression pattern.
- `match = re.search(pattern, test_string)`: This uses the `re.search()` function to search for a match between the regular expression pattern and the test string.
- `if match:`: This checks if a match was found.
- `print("Match found!")`: This prints a message if a match was found.
- `print("No match found!")`: This prints a message if no match was found.

For more information about regular expressions in Python, see the [Python documentation](https://docs.python.org/3/library/re.html).

onelinerhub: [How to match a question mark in Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-question-mark-in-python-regex)
# How to do an exact match with regex in Python?
// plain

To do an exact match with regex in Python, you can use the `re.match()` function. This function takes a regular expression pattern and a string as arguments and returns a match object if there is a match.

## Example code

```
import re

pattern = r"Hello"
string = "Hello World"

match = re.match(pattern, string)

if match:
  print("Match found:", match.group())
else:
  print("No match found")
```

## Output example

```
Match found: Hello
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.match()` function
- `pattern = r"Hello"`: defines the regular expression pattern to match
- `string = "Hello World"`: defines the string to match against
- `match = re.match(pattern, string)`: calls the `re.match()` function with the pattern and string as arguments
- `if match:`: checks if a match was found
- `print("Match found:", match.group())`: prints the matched string
- `else:`: runs if no match was found
- `print("No match found")`: prints a message if no match was found

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [re.match()](https://docs.python.org/3/library/re.html#re.match)

onelinerhub: [How to do an exact match with regex in Python?](https://onelinerhub.com/python-regex/how-to-do-an-exact-match-with-regex-in-python)
# How to perform a zero length match with Python Regex?
// plain

Zero length matches are matches that do not consume any characters. They can be used to find the position of a pattern in a string. In Python, this can be done using the `re.search()` function with the `\b` metacharacter.

```
import re

string = "Hello World"

match = re.search(r"\b", string)

if match:
    print("Match found at position:", match.start())
```

## Output example

```
Match found at position: 0
```

The code above uses the `re.search()` function to search for a zero length match in the string `"Hello World"`. The `\b` metacharacter is used to indicate a zero length match. If a match is found, the `match.start()` method is used to print the position of the match.

## Code explanation

- `import re`: imports the `re` module which contains the `re.search()` function
- `string = "Hello World"`: creates a string to search for a zero length match
- `match = re.search(r"\b", string)`: uses the `re.search()` function to search for a zero length match indicated by the `\b` metacharacter
- `if match:`: checks if a match was found
- `print("Match found at position:", match.start())`: prints the position of the match if one was found

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Zero Length Matches](https://www.regular-expressions.info/zerolength.html)

onelinerhub: [How to perform a zero length match with Python Regex?](https://onelinerhub.com/python-regex/how-to-perform-a-zero-length-match-with-python-regex)
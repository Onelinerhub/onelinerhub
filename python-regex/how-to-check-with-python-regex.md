# How to check with Python regex?
// plain

Python regex can be used to check for patterns in strings. It is a powerful tool for text processing.

## Example code

```
import re

string = "Hello World"

# Check if the string contains the word "Hello"
if re.search("Hello", string):
    print("Found a match!")
```

## Output example

```
Found a match!
```

## Code explanation

- `import re`: imports the Python regex module
- `string = "Hello World"`: creates a string variable
- `if re.search("Hello", string):`: checks if the string contains the word "Hello"
- `print("Found a match!")`: prints the message "Found a match!" if the string contains the word "Hello"

## Helpful links
- [Python Regex Documentation](https://docs.python.org/3/library/re.html)
- [Regex Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to check with Python regex?](https://onelinerhub.com/python-regex/how-to-check-with-python-regex)
# How to replace all using Python regex?
// plain

Regex (or Regular Expressions) is a powerful tool for string manipulation in Python. It can be used to replace all occurrences of a given pattern in a string with a different string.

## Example code

```
import re

text = "This is a test string"

# Replace all occurrences of 'test' with 'example'
new_text = re.sub('test', 'example', text)

print(new_text)
```

## Output example

```
This is a example string
```

## Code explanation

- `import re`: imports the Python regex module
- `re.sub('test', 'example', text)`: uses the `sub()` function from the regex module to replace all occurrences of 'test' with 'example' in the string `text`
- `print(new_text)`: prints the new string with all occurrences of 'test' replaced with 'example'

## Helpful links
- [Python Regex Documentation](https://docs.python.org/3/library/re.html)
- [Regex Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to replace all using Python regex?](https://onelinerhub.com/python-regex/how-to-replace-all-using-python-regex)
# How to replace using Python regex?
// plain

Python's `re` module provides a powerful set of tools for performing regular expression (regex) operations. To replace using Python regex, the `re.sub()` function can be used. This function takes three arguments: the pattern to search for, the replacement string, and the string to search in.

## Example code

```
import re

text = "This is a test string"

new_text = re.sub(r"test", "sample", text)

print(new_text)
```

## Output example

```
This is a sample string
```

## Code explanation

- `import re`: imports the `re` module, which provides the tools for performing regex operations
- `re.sub(r"test", "sample", text)`: searches for the pattern `test` in the string `text` and replaces it with `sample`
- `print(new_text)`: prints the new string with the replaced pattern

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [re.sub()](https://docs.python.org/3/library/re.html#re.sub)

onelinerhub: [How to replace using Python regex?](https://onelinerhub.com/python-regex/how-to-replace-using-python-regex)
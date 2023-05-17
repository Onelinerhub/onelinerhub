# How to split using Python regex?
// plain

Python's `re` module provides a powerful set of tools for working with regular expressions. The `re.split()` function can be used to split a string into a list of substrings based on a regular expression pattern.

```
import re

string = "This is a string to split"

result = re.split("\s+", string)

print(result)
```

## Output example

```
['This', 'is', 'a', 'string', 'to', 'split']
```

The code above uses the `re.split()` function to split the string `"This is a string to split"` into a list of substrings based on the regular expression pattern `\s+`, which matches one or more whitespace characters.

Parts of the code:

- `import re`: imports the `re` module, which provides tools for working with regular expressions.
- `string = "This is a string to split"`: assigns the string to be split to the variable `string`.
- `re.split("\s+", string)`: uses the `re.split()` function to split the string `string` into a list of substrings based on the regular expression pattern `\s+`, which matches one or more whitespace characters.
- `print(result)`: prints the resulting list of substrings.

## Helpful links

- [Python Regular Expression Quick Guide](https://www.tutorialspoint.com/python/python_reg_expressions.htm)
- [Python re Module Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to split using Python regex?](https://onelinerhub.com/python-regex/how-to-split-using-python-regex)
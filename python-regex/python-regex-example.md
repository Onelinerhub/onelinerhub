# Python regex example
// plain

Python supports regular expressions through the `re` module. Regular expressions are a powerful language for matching text patterns.

## Example code

```python
import re

# Match a literal string
result = re.search(r"Hello World", "Hello World")

# Print the result
print(result)
```

## Output example

```
<re.Match object; span=(0, 11), match='Hello World'>
```

## Code explanation

- `import re`: imports the `re` module which provides support for regular expressions
- `re.search(r"Hello World", "Hello World")`: searches for the literal string `Hello World` in the string `Hello World`
- `print(result)`: prints the result of the search

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [Python regex example](https://onelinerhub.com/python-regex/python-regex-example)
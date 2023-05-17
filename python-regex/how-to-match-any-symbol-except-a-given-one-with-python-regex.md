# How to match any symbol except a given one with Python regex?
// plain

To match any symbol except a given one with Python regex, you can use the `[^symbol]` syntax. This syntax will match any character except the one specified. For example, to match any character except `a`, you can use the following code:

```
import re

string = "Hello World!"

match = re.search(r"[^a]", string)

print(match.group())
```

## Output example

```
H
```

The code above uses the following parts:

- `import re`: imports the `re` module which provides regular expression matching operations.
- `string = "Hello World!"`: creates a string variable to use for the example.
- `match = re.search(r"[^a]", string)`: uses the `re.search()` function to search for any character except `a` in the `string` variable.
- `print(match.group())`: prints the first match found.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

onelinerhub: [How to match any symbol except a given one with Python regex?](https://onelinerhub.com/python-regex/how-to-match-any-symbol-except-a-given-one-with-python-regex)
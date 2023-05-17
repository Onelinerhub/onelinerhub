# How to compile a regex in Python?
// plain

Compiling a regular expression in Python is a process of converting a regular expression pattern into a regular expression object. This object can be used for pattern matching.

```
import re

# Compile the regular expression
pattern = re.compile("\d+")

# Use the compiled regular expression
result = pattern.match("123")

print(result)
```

## Output example

```
<re.Match object; span=(0, 3), match='123'>
```

The code above consists of the following parts:

1. `import re` - imports the `re` module which contains the functions for working with regular expressions.
2. `pattern = re.compile("\d+")` - compiles the regular expression pattern `\d+` into a regular expression object.
3. `result = pattern.match("123")` - uses the compiled regular expression object to match the string `123`.
4. `print(result)` - prints the result of the match.

## Helpful links

- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to compile a regex in Python?](https://onelinerhub.com/python-regex/how-to-compile-a-regex-in-python)
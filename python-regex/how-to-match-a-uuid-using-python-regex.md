# How to match a UUID using Python regex?
// plain

Python regex can be used to match a UUID using the `re` module. The following example code will match a UUID:

```python
import re

pattern = re.compile(r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)

match = pattern.match('12345678-1234-4abc-8bcd-123456789abc')

if match:
    print('UUID matched!')
```

## Output example

```
UUID matched!
```

The code consists of the following parts:

1. `import re`: imports the `re` module which provides regular expression matching operations.
2. `pattern = re.compile(r'[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z', re.I)`: compiles the regular expression pattern which matches a UUID. The pattern consists of 8 hexadecimal digits, followed by an optional hyphen, followed by 4 hexadecimal digits, followed by an optional hyphen, followed by 4 hexadecimal digits, followed by an optional hyphen, followed by 3 hexadecimal digits, followed by an optional hyphen, followed by 12 hexadecimal digits. The `re.I` flag makes the pattern case-insensitive.
3. `match = pattern.match('12345678-1234-4abc-8bcd-123456789abc')`: attempts to match the pattern against the given string.
4. `if match:`: checks if the pattern matched the given string.
5. `print('UUID matched!')`: prints a message if the pattern matched the given string.

## Helpful links

- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match a UUID using Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-uuid-using-python-regex)
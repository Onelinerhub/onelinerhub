# How to make a case insensitive match with Python regex?
// plain

To make a case insensitive match with Python regex, use the `re.IGNORECASE` flag. This flag will cause the regex engine to ignore the case of the characters when matching.

## Example code

```
import re

pattern = re.compile(r'[A-Z]+', re.IGNORECASE)

match = pattern.search('aBc')

print(match.group())
```

## Output example

```
aBc
```

## Code explanation

- `import re`: imports the `re` module which contains the regex engine
- `re.compile(r'[A-Z]+', re.IGNORECASE)`: compiles the regex pattern `[A-Z]+` with the `re.IGNORECASE` flag
- `pattern.search('aBc')`: searches the string `aBc` for the compiled regex pattern
- `match.group()`: prints the matched string

## Helpful links
- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to make a case insensitive match with Python regex?](https://onelinerhub.com/python-regex/how-to-make-a-case-insensitive-match-with-python-regex)
# How to use negative lookbehind in Python regex?
// plain

Negative lookbehind is a feature of regular expressions that allows you to match a pattern only if it is not preceded by another pattern. It is supported in Python through the `re` module.

## Example

```
import re

# Match any word that is not preceded by "not"
pattern = r"(?<!not)\b\w+\b"

string = "This is not a test"

match = re.search(pattern, string)

if match:
    print(match.group())
```

## Output example

```
This
```

## Code explanation

- `(?<!not)` - Negative lookbehind assertion that matches only if the pattern is not preceded by "not"
- `\b\w+\b` - Matches any word
- `re.search(pattern, string)` - Searches for the pattern in the string
- `match.group()` - Returns the matched pattern

## Helpful links
- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)
- [Negative Lookbehind Tutorial](https://www.regular-expressions.info/lookaround.html)

onelinerhub: [How to use negative lookbehind in Python regex?](https://onelinerhub.com/python-regex/how-to-use-negative-lookbehind-in-python-regex)
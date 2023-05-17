# How to match a range between two characters with Python regex?
// plain

To match a range between two characters with Python regex, you can use the `[]` character class. This character class allows you to specify a range of characters to match. For example, the following code will match any character between `a` and `z`:
```
import re

pattern = re.compile('[a-z]')

print(pattern.match('b'))
```
## Output example

```
<re.Match object; span=(0, 1), match='b'>
```

The code consists of the following parts:

1. `import re`: This imports the `re` module, which provides regular expression matching operations.
2. `pattern = re.compile('[a-z]')`: This creates a regular expression pattern object that will match any character between `a` and `z`.
3. `print(pattern.match('b'))`: This prints the result of matching the character `b` against the pattern.

## Helpful links

- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match a range between two characters with Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-range-between-two-characters-with-python-regex)
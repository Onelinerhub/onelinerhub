# How to match any letter with Python regex?
// plain

To match any letter with Python regex, you can use the `\w` character class. This character class will match any alphanumeric character, including both upper and lowercase letters.

## Example code

```
import re

pattern = re.compile(r'\w')

string = 'Hello World!'

matches = pattern.findall(string)
```

## Output example

```
['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
```

## Code explanation

- `import re`: imports the `re` module, which contains the functions needed for regular expression matching
- `pattern = re.compile(r'\w')`: compiles the regular expression pattern `\w`, which matches any alphanumeric character
- `string = 'Hello World!'`: sets the string to be matched
- `matches = pattern.findall(string)`: finds all matches of the pattern in the string

## Helpful links
- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression Character Classes](https://www.regular-expressions.info/charclass.html)

onelinerhub: [How to match any letter with Python regex?](https://onelinerhub.com/python-regex/how-to-match-any-letter-with-python-regex)
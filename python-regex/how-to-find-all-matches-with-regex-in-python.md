# How to find all matches with regex in Python?
// plain

To find all matches with regex in Python, you can use the `re.findall()` function. This function takes two arguments: the pattern to search for, and the string to search in.

## Example code

```
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "The.*dog"

matches = re.findall(pattern, string)
print(matches)
```

## Output example

```
['The quick brown fox jumps over the lazy dog']
```

## Code explanation

- `import re`: imports the `re` module, which contains the `findall()` function.
- `string`: the string to search in.
- `pattern`: the pattern to search for.
- `re.findall(pattern, string)`: searches for all matches of the pattern in the string.
- `print(matches)`: prints the matches.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [re — Regular expression operations](https://docs.python.org/3/library/re.html#module-re)

onelinerhub: [How to find all matches with regex in Python?](https://onelinerhub.com/python-regex/how-to-find-all-matches-with-regex-in-python)
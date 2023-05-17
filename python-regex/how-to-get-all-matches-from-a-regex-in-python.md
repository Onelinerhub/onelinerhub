# How to get all matches from a regex in Python?
// plain

To get all matches from a regex in Python, you can use the `re.findall()` function. This function takes two arguments: the pattern to search for and the string to search in. It returns a list of all matches found.

## Example code

```
import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"\w+"

matches = re.findall(pattern, string)
print(matches)
```

## Output example

```
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

## Code explanation

- `import re`: imports the `re` module which contains the `findall()` function.
- `string = "The quick brown fox jumps over the lazy dog"`: defines the string to search in.
- `pattern = r"\w+"`: defines the pattern to search for.
- `matches = re.findall(pattern, string)`: calls the `findall()` function to search for the pattern in the string and store the matches in the `matches` variable.
- `print(matches)`: prints the matches found.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [re.findall()](https://docs.python.org/3/library/re.html#re.findall)

onelinerhub: [How to get all matches from a regex in Python?](https://onelinerhub.com/python-regex/how-to-get-all-matches-from-a-regex-in-python)
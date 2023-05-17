# How to regex match excluding a word in Python?
// plain

To regex match excluding a word in Python, you can use the `re.search()` function with a negative lookahead assertion. The negative lookahead assertion is a special syntax that allows you to specify a pattern that should not be matched.

For example, the following code will match any string that contains the word `cat` but not the word `dog`:
```
import re

string = 'The cat is sleeping'

match = re.search(r'cat(?!.*dog)', string)

if match:
    print('Match found:', match.group())
```

## Output example

```
Match found: cat
```

The code consists of the following parts:

- `import re`: imports the `re` module, which provides functions for working with regular expressions.
- `string = 'The cat is sleeping'`: defines a string to search.
- `match = re.search(r'cat(?!.*dog)', string)`: uses the `re.search()` function to search for the pattern `cat(?!.*dog)` in the string. The `(?!.*dog)` part is a negative lookahead assertion, which means that the pattern should not be followed by the word `dog`.
- `if match:`: checks if a match was found.
- `print('Match found:', match.group())`: prints the matched string.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Negative Lookahead Assertions](https://www.regular-expressions.info/lookaround.html)

onelinerhub: [How to regex match excluding a word in Python?](https://onelinerhub.com/python-regex/how-to-regex-match-excluding-a-word-in-python)
# How to match a text from file with Python regex?
// plain

Matching a text from a file with Python regex is a powerful way to search for patterns in a text. It can be used to find specific words, phrases, or even more complex patterns.

```
import re

# Open the file
f = open('text.txt', 'r')

# Read the file
text = f.read()

# Find all matches of the pattern
matches = re.findall(r'pattern', text)

# Print the matches
print(matches)
```

```
['pattern', 'pattern', 'pattern']
```

The code above uses the `re` module to open a file, read it, and find all matches of a given pattern. The `findall()` function takes a regular expression as an argument and returns a list of all matches.

- `import re`: imports the `re` module which provides functions for working with regular expressions
- `f = open('text.txt', 'r')`: opens the file `text.txt` in read mode
- `text = f.read()`: reads the contents of the file and stores it in the `text` variable
- `matches = re.findall(r'pattern', text)`: finds all matches of the pattern `pattern` in the `text` variable and stores them in the `matches` variable
- `print(matches)`: prints the matches

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match a text from file with Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-text-from-file-with-python-regex)
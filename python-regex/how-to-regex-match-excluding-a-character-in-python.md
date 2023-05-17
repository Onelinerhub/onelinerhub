# How to regex match excluding a character in Python?
// plain

To regex match excluding a character in Python, you can use the `re.search()` function with the `^` and `$` symbols. The `^` symbol indicates the start of the string, and the `$` symbol indicates the end of the string. Any character that is not the character you want to exclude will be matched.

For example, to match a string that starts with `Hello` and ends with `World` but does not contain the letter `a`, you can use the following code:

```python
import re

string = "Hello World"

if re.search("^Hello[^a]*World$", string):
    print("Match found!")
```

## Output example

```
Match found!
```

The code consists of the following parts:

1. `import re`: imports the `re` module which contains the `re.search()` function.
2. `string = "Hello World"`: assigns the string to be matched to the `string` variable.
3. `if re.search("^Hello[^a]*World$", string):`: uses the `re.search()` function to search for a match in the `string` variable. The regex pattern `^Hello[^a]*World$` matches any string that starts with `Hello`, does not contain the letter `a`, and ends with `World`.
4. `print("Match found!")`: prints the message `Match found!` if a match is found.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)

onelinerhub: [How to regex match excluding a character in Python?](https://onelinerhub.com/python-regex/how-to-regex-match-excluding-a-character-in-python)
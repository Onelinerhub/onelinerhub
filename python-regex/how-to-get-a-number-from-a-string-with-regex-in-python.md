# How to get a number from a string with regex in Python?
// plain

Regex (Regular Expression) is a powerful tool for string manipulation in Python. It can be used to extract a number from a string.

## Example code

```
import re

string = 'The number is 1234'

# Extract the number
number = re.findall('\d+', string)

# Print the number
print(number)
```

## Output example

```
['1234']
```

## Code explanation

- `import re`: imports the regex module
- `re.findall('\d+', string)`: searches for one or more digits in the string and returns a list of matches
- `print(number)`: prints the extracted number

## Helpful links
- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to get a number from a string with regex in Python?](https://onelinerhub.com/python-regex/how-to-get-a-number-from-a-string-with-regex-in-python)
# How to extract found values with Python regex?
// plain

Python regex can be used to extract found values from a string. The `re.findall()` function can be used to find all matches in a string and return them as a list.

## Example code

```
import re

string = "The cat in the hat"

matches = re.findall("cat", string)

print(matches)
```

## Output example

```
['cat']
```

## Code explanation

- `import re`: imports the Python regex module
- `string = "The cat in the hat"`: assigns the string to be searched
- `matches = re.findall("cat", string)`: uses the `re.findall()` function to search for the pattern "cat" in the string and assign the matches to the `matches` variable
- `print(matches)`: prints the matches found

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/howto/regex.html)
- [re — Regular expression operations](https://docs.python.org/3/library/re.html)

onelinerhub: [How to extract found values with Python regex?](https://onelinerhub.com/python-regex/how-to-extract-found-values-with-python-regex)
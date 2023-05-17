# How to use a regex capture group in Python?
// plain

Regex capture groups are used to group parts of a regular expression together so that they can be referenced later. In Python, capture groups are accessed using the `group()` method of the `Match` object.

## Example code

```
import re

text = "The cat in the hat"

match = re.search(r"(\w+) in the (\w+)", text)

if match:
    print(match.group(1))
    print(match.group(2))
```

## Output example

```
cat
hat
```

## Code explanation


1. `import re`: This imports the `re` module which contains the functions needed to use regular expressions in Python.
2. `text = "The cat in the hat"`: This creates a string variable containing the text to be searched.
3. `match = re.search(r"(\w+) in the (\w+)", text)`: This uses the `re.search()` function to search for a pattern in the text. The pattern is enclosed in parentheses to create two capture groups.
4. `if match:`: This checks if a match was found.
5. `print(match.group(1))`: This prints the first capture group.
6. `print(match.group(2))`: This prints the second capture group.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python re.search() Method](https://www.tutorialspoint.com/python/re_search.htm)
- [Python re.Match Object](https://www.tutorialspoint.com/python/match_object.htm)

onelinerhub: [How to use a regex capture group in Python?](https://onelinerhub.com/python-regex/how-to-use-a-regex-capture-group-in-python)
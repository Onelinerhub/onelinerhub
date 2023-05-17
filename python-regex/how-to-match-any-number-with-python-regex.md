# How to match any number with Python regex?
// plain

Python regex can be used to match any number. The `\d` character class can be used to match any digit from 0 to 9. The `+` quantifier can be used to match one or more digits. The following example code block shows how to match any number with Python regex:

```
import re

pattern = r"\d+"

string = "There are 12 cats and 15 dogs"

match = re.search(pattern, string)

if match:
    print(match.group())
```

The output of the example code is:

```
12
```

## Code explanation


- `import re`: This imports the `re` module which provides regular expression matching operations.

- `pattern = r"\d+"`: This defines the regular expression pattern which matches one or more digits.

- `string = "There are 12 cats and 15 dogs"`: This defines the string which will be searched for matches.

- `match = re.search(pattern, string)`: This searches the string for a match to the regular expression pattern.

- `if match:`: This checks if a match was found.

- `print(match.group())`: This prints the matched text.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match any number with Python regex?](https://onelinerhub.com/python-regex/how-to-match-any-number-with-python-regex)
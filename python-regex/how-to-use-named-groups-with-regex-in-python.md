# How to use named groups with regex in Python?
// plain

Named groups are a powerful tool for regex in Python. They allow you to assign names to parts of a regular expression, making it easier to read and maintain. To use named groups, you need to use the syntax `(?P<name>pattern)`, where `name` is the name of the group and `pattern` is the regular expression pattern.

For example, the following code uses named groups to match a date string:
```
import re

date_regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")

date_string = "2020-05-15"

match = date_regex.match(date_string)

print(match.group("year"))  # Output: 2020
print(match.group("month")) # Output: 05
print(match.group("day"))   # Output: 15
```

## Code explanation


- `(?P<name>pattern)`: This is the syntax for creating a named group. `name` is the name of the group and `pattern` is the regular expression pattern.
- `date_regex = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")`: This line creates a regular expression object with three named groups: `year`, `month`, and `day`.
- `match = date_regex.match(date_string)`: This line uses the regular expression object to match the date string.
- `print(match.group("year"))`: This line prints the value of the `year` group from the match.

## Helpful links

- [Python Regular Expression Tutorial](https://realpython.com/regex-python/)
- [Python re Module Documentation](https://docs.python.org/3/library/re.html)

onelinerhub: [How to use named groups with regex in Python?](https://onelinerhub.com/python-regex/how-to-use-named-groups-with-regex-in-python)
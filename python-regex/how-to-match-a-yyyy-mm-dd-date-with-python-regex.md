# How to match a YYYY-MM-DD date with Python Regex?
// plain

Python Regex can be used to match a YYYY-MM-DD date. The following example code block shows how to do this:
```
import re

date_string = '2020-01-01'

date_regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

match = date_regex.match(date_string)

if match:
  print('Year:', match.group(1))
  print('Month:', match.group(2))
  print('Day:', match.group(3))
```
The output of the example code is:
```
Year: 2020
Month: 01
Day: 01
```
## Code explanation

- `import re`: imports the Python Regex module
- `date_string = '2020-01-01'`: sets the date string to match
- `date_regex = re.compile(r'(\d{4})-(\d{2})-(\d{2})')`: compiles the Regex pattern to match the date string
- `match = date_regex.match(date_string)`: matches the date string with the Regex pattern
- `if match:`: checks if the date string matches the Regex pattern
- `print('Year:', match.group(1))`: prints the year part of the date string
- `print('Month:', match.group(2))`: prints the month part of the date string
- `print('Day:', match.group(3))`: prints the day part of the date string

## Helpful links
- [Python Regex Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match a YYYY-MM-DD date with Python Regex?](https://onelinerhub.com/python-regex/how-to-match-a-yyyy-mm-dd-date-with-python-regex)
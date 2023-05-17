# How to match a float with regex in Python?
// plain

Matching a float with regex in Python can be done using the `re` module. The following example code block shows how to match a float with regex:
```
import re

float_regex = re.compile(r'[+-]?\d*\.\d+')

float_match = float_regex.match('3.14')

print(float_match.group())
```
The output of the example code is:
```
3.14
```
## Code explanation


1. `import re`: imports the `re` module which provides regular expression matching operations.
2. `float_regex = re.compile(r'[+-]?\d*\.\d+')`: compiles a regular expression pattern to match a float. The pattern `[+-]?\d*\.\d+` matches a float with an optional sign (+ or -), followed by any number of digits, followed by a decimal point, followed by one or more digits.
3. `float_match = float_regex.match('3.14')`: uses the compiled regular expression pattern to match the string `3.14`.
4. `print(float_match.group())`: prints the matched float.

## Helpful links

- [Python Regular Expression Quick Guide](https://www.rexegg.com/regex-quickstart.html)
- [Python re Module](https://docs.python.org/3/library/re.html)

onelinerhub: [How to match a float with regex in Python?](https://onelinerhub.com/python-regex/how-to-match-a-float-with-regex-in-python)
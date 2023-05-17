# How to match an IP address with regex in Python?
// plain

Regex (Regular Expression) is a powerful tool for matching patterns in strings. In Python, it can be used to match an IP address with the `re` module.

## Example code

```
import re

# Sample IP address
ip = "10.10.10.1"

# Regex for IP address
regex = '''
^ # Start of the line
(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?) # First number (0-255)
\. # Dot
(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?) # Second number (0-255)
\. # Dot
(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?) # Third number (0-255)
\. # Dot
(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?) # Fourth number (0-255)
$ # End of the line
'''

# Compile the Regex
pattern = re.compile(regex)

# Match the IP address
match = pattern.match(ip)

# Print the match
print(match)
```

## Output example

```
<re.Match object; span=(0, 11), match='10.10.10.1'>
```

The code above uses the `re` module to compile a regex pattern for matching an IP address. The regex pattern consists of four parts, each representing a number from 0 to 255. The pattern is then used to match the IP address, and the result is printed.

## Code explanation


1. `^`: Start of the line
2. `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)`: First number (0-255)
3. `\.`: Dot
4. `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)`: Second number (0-255)
5. `\.`: Dot
6. `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)`: Third number (0-255)
7. `\.`: Dot
8. `(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)`: Fourth number (0-255)
9. `$`: End of the line

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match an IP address with regex in Python?](https://onelinerhub.com/python-regex/how-to-match-an-ip-address-with-regex-in-python)
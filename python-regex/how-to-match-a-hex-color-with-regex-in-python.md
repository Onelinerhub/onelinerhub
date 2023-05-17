# How to match a hex color with regex in Python?
// plain

Regex can be used to match a hex color in Python. The regex pattern for a hex color is `#[A-Fa-f0-9]{6}`. This pattern will match any valid hex color code, including the # symbol.

## Example code

```
import re

hex_color_regex = re.compile(r'#[A-Fa-f0-9]{6}')

hex_color = '#FF0000'

if hex_color_regex.match(hex_color):
    print('Valid hex color')
else:
    print('Invalid hex color')
```

## Output example

```
Valid hex color
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.compile()` function used to create the regex pattern.
- `hex_color_regex = re.compile(r'#[A-Fa-f0-9]{6}')`: creates a regex pattern object using the `re.compile()` function. The pattern `#[A-Fa-f0-9]{6}` will match any valid hex color code, including the # symbol.
- `hex_color = '#FF0000'`: sets the variable `hex_color` to a valid hex color code.
- `if hex_color_regex.match(hex_color):`: checks if the `hex_color` variable matches the regex pattern.
- `print('Valid hex color')`: prints the message `Valid hex color` if the `hex_color` variable matches the regex pattern.
- `print('Invalid hex color')`: prints the message `Invalid hex color` if the `hex_color` variable does not match the regex pattern.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regex Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to match a hex color with regex in Python?](https://onelinerhub.com/python-regex/how-to-match-a-hex-color-with-regex-in-python)
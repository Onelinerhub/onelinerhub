# How to quote in Python regex?
// plain

Python regex can be used to quote strings. To quote a string, use the `re.escape()` function. This function takes a string as an argument and returns a string with all non-alphanumeric characters escaped.

For example:
```
import re

string = "This is a string with special characters!"

escaped_string = re.escape(string)

print(escaped_string)
```

## Output example

```
This\ is\ a\ string\ with\ special\ characters\!
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.escape()` function
- `string = "This is a string with special characters!"`: assigns the string to be quoted to the `string` variable
- `escaped_string = re.escape(string)`: calls the `re.escape()` function and assigns the returned string to the `escaped_string` variable
- `print(escaped_string)`: prints the escaped string

## Helpful links
- [Python Regular Expression Documentation](https://docs.python.org/3/library/re.html)
- [Python re.escape() Documentation](https://docs.python.org/3/library/re.html#re.escape)

onelinerhub: [How to quote in Python regex?](https://onelinerhub.com/python-regex/how-to-quote-in-python-regex)
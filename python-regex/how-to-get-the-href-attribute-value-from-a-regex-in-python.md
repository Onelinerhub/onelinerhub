# How to get the href attribute value from a regex in Python?
// plain

The href attribute value from a regex can be obtained in Python using the `re.findall()` function. This function takes a regular expression pattern and a string as arguments and returns a list of all non-overlapping matches in the string.

## Example code

```
import re

html_string = '<a href="https://www.example.com">Example</a>'

href_value = re.findall(r'href="(.*?)"', html_string)

print(href_value)
```

## Output example

```
['https://www.example.com']
```

## Code explanation


1. `import re`: This imports the `re` module which provides regular expression matching operations.
2. `html_string = '<a href="https://www.example.com">Example</a>'`: This is the HTML string from which the href attribute value needs to be extracted.
3. `href_value = re.findall(r'href="(.*?)"', html_string)`: This uses the `re.findall()` function to extract the href attribute value from the HTML string. The regular expression pattern `r'href="(.*?)"'` matches the href attribute value and the `.*?` part captures the value.
4. `print(href_value)`: This prints the href attribute value.

## Helpful links

1. [Python Regular Expressions](https://docs.python.org/3/library/re.html)
2. [Python re.findall()](https://docs.python.org/3/library/re.html#re.findall)

onelinerhub: [How to get the href attribute value from a regex in Python?](https://onelinerhub.com/python-regex/how-to-get-the-href-attribute-value-from-a-regex-in-python)
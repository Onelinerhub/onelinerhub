# How to match HTML tags with regex in Python?
// plain

Matching HTML tags with regex in Python can be done using the `re` module. The `re.findall()` function can be used to find all occurrences of a pattern in a string. For example, the following code will find all HTML tags in a string:
```
import re

html_string = "<p>This is a paragraph</p><h1>This is a heading</h1>"

tags = re.findall(r"<[^>]*>", html_string)

print(tags)
```
## Output example

```
['<p>', '</p>', '<h1>', '</h1>']
```

The code works by using the `re.findall()` function to search for all occurrences of a pattern in a string. The pattern used is `r"<[^>]*>"`, which matches any HTML tag. The `[^>]` part of the pattern means that any character that is not a `>` character can be matched.

The output of the code is a list of all the HTML tags found in the string.

## Code explanation

- `re.findall()`: This function searches for all occurrences of a pattern in a string.
- `r"<[^>]*>"`: This is the pattern used to match HTML tags. The `[^>]` part of the pattern means that any character that is not a `>` character can be matched.

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match HTML tags with regex in Python?](https://onelinerhub.com/python-regex/how-to-match-html-tags-with-regex-in-python)
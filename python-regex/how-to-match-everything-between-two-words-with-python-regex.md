# How to match everything between two words with Python regex?
// plain

To match everything between two words with Python regex, you can use the `re.findall()` function. This function takes a regular expression pattern and a string as arguments and returns a list of all non-overlapping matches of the pattern in the string.

For example, to match everything between two words `start` and `end`, you can use the following code:
```
import re

text = "This is a start sentence. This is an end sentence."

matches = re.findall(r"start(.*?)end", text)
print(matches)
```
The output of the above code will be:
```
[' sentence. This is an ']
```

The code consists of the following parts:

1. `import re`: This imports the `re` module which provides regular expression matching operations.
2. `text = "This is a start sentence. This is an end sentence."`: This is the string in which we will search for the pattern.
3. `matches = re.findall(r"start(.*?)end", text)`: This uses the `re.findall()` function to search for the pattern `start(.*?)end` in the string `text`. The `.*?` part of the pattern matches any character (`.`) zero or more times (`*`) in a non-greedy manner (`?`).
4. `print(matches)`: This prints the list of matches found by the `re.findall()` function.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to match everything between two words with Python regex?](https://onelinerhub.com/python-regex/how-to-match-everything-between-two-words-with-python-regex)
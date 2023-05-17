# How to use "and" condition in Python regex?
// plain

The `and` condition can be used in Python regex to match two patterns at the same time. For example, the following code block will match strings that contain both `cat` and `dog`:
```
import re

pattern = re.compile(r'cat.*dog', re.IGNORECASE)

if pattern.search('The cat and the dog'):
    print('Match found!')
```

## Output example

```
Match found!
```

The code above consists of the following parts:

1. `import re`: This imports the `re` module, which provides access to the regular expression operations.
2. `pattern = re.compile(r'cat.*dog', re.IGNORECASE)`: This creates a regular expression object with the pattern `cat.*dog` and the `re.IGNORECASE` flag, which makes the pattern case-insensitive.
3. `if pattern.search('The cat and the dog'):`: This uses the `search()` method of the `pattern` object to search for the pattern in the given string.
4. `print('Match found!')`: This prints the message `Match found!` if the pattern is found in the string.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python re Module](https://docs.python.org/3/library/re.html#module-re)

onelinerhub: [How to use "and" condition in Python regex?](https://onelinerhub.com/python-regex/how-to-use--and--condition-in-python-regex)
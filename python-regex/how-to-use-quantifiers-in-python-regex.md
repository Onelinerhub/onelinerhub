# How to use quantifiers in Python regex?
// plain

Quantifiers are used in Python regex to specify the number of times a character, group, or character class can appear in the searched text.

For example, the regex `a{2,4}` will match any string that contains between 2 and 4 `a` characters.

```
import re

# Match strings with between 2 and 4 a characters
pattern = re.compile(r'a{2,4}')

# Test strings
test_strings = ['aa', 'aaa', 'aaaa', 'aaaaa']

# Print matches
for test_string in test_strings:
    if pattern.search(test_string):
        print('{} matches'.format(test_string))
    else:
        print('{} does not match'.format(test_string))
```

## Output example


```
aa matches
aaa matches
aaaa matches
aaaaa does not match
```

The code above uses the `re.compile()` function to create a regex pattern object, and the `pattern.search()` method to search for matches in the test strings. The `{2,4}` quantifier specifies that the pattern should match strings with between 2 and 4 `a` characters.

Parts of the code:

- `re.compile(r'a{2,4}')`: creates a regex pattern object that will match strings with between 2 and 4 `a` characters
- `pattern.search(test_string)`: searches for matches in the test strings
- `{2,4}`: quantifier that specifies the number of times the character, group, or character class can appear in the searched text

## Helpful links

- [Python Regex Cheat Sheet](https://www.pybloggers.com/wp-content/uploads/2018/07/Python-Regex-Cheat-Sheet.pdf)
- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)

onelinerhub: [How to use quantifiers in Python regex?](https://onelinerhub.com/python-regex/how-to-use-quantifiers-in-python-regex)
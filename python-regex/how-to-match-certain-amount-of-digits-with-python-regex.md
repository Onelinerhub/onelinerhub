# How to match certain amount of digits with Python regex?
// plain

Python regex can be used to match certain amount of digits. The `\d` character class is used to match any single digit. To match a specific amount of digits, the `{n}` quantifier can be used, where `n` is the number of digits to match. For example, to match exactly 5 digits, the regex `\d{5}` can be used.

```
import re

# Match exactly 5 digits
pattern = r"\d{5}"

# Test string
test_string = "1234567890"

# Match the pattern
result = re.match(pattern, test_string)

# Print the result
print(result)
```

## Output example

```
<re.Match object; span=(0, 5), match='12345'>
```

## Code explanation

- `\d`: character class used to match any single digit
- `{n}`: quantifier used to match a specific amount of digits, where `n` is the number of digits to match

## Helpful links
- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to match certain amount of digits with Python regex?](https://onelinerhub.com/python-regex/how-to-match-certain-amount-of-digits-with-python-regex)
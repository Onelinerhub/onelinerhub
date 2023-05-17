# How to remove numbers from a string using Python regex?
// plain

Using Python regex, numbers can be removed from a string by using the `re.sub()` function. This function takes two arguments, the pattern to be matched and the replacement string. The pattern can be specified using the `\d` character class, which matches any digit.

```
import re

string = "This is a string with 123 numbers"

result = re.sub(r'\d+', '', string)

print(result)
```

## Output example

```
This is a string with  numbers
```

The code above consists of the following parts:

1. `import re`: This imports the `re` module, which provides functions for working with regular expressions.
2. `string = "This is a string with 123 numbers"`: This creates a string variable containing the string to be processed.
3. `result = re.sub(r'\d+', '', string)`: This uses the `re.sub()` function to replace any digits in the string with an empty string.
4. `print(result)`: This prints the result of the substitution.

## Helpful links

- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

onelinerhub: [How to remove numbers from a string using Python regex?](https://onelinerhub.com/python-regex/how-to-remove-numbers-from-a-string-using-python-regex)
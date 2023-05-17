# How to replace a certain group using Python regex?
// plain

Regex (regular expressions) can be used to replace a certain group of characters in a string using Python. To do this, the `re.sub()` function can be used. This function takes three arguments: the pattern to search for, the replacement string, and the string to search in.

## Example code

```
import re

string = "Hello World!"

new_string = re.sub("World", "Universe", string)

print(new_string)
```

## Output example

```
Hello Universe!
```

## Code explanation

- `import re`: imports the `re` module which contains the `re.sub()` function
- `string = "Hello World!"`: assigns the string to be searched to the `string` variable
- `new_string = re.sub("World", "Universe", string)`: uses the `re.sub()` function to search for the pattern `World` in the `string` variable and replace it with `Universe`
- `print(new_string)`: prints the new string with the replaced pattern

## Helpful links
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [re.sub()](https://docs.python.org/3/library/re.html#re.sub)

onelinerhub: [How to replace a certain group using Python regex?](https://onelinerhub.com/python-regex/how-to-replace-a-certain-group-using-python-regex)
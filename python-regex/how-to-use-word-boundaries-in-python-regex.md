# How to use word boundaries in Python Regex?
// plain

Word boundaries are used in Python Regex to match the beginning or end of a word.

```
import re

# Match the beginning of a word
result = re.search(r'\bcat', 'The cat in the hat')
print(result.group())
```

## Output example

```
cat
```

## Code explanation

- `\b`: A word boundary which matches the beginning or end of a word
- `cat`: The word to match
- `The cat in the hat`: The string to search

## Helpful links
- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

onelinerhub: [How to use word boundaries in Python Regex?](https://onelinerhub.com/python-regex/how-to-use-word-boundaries-in-python-regex)
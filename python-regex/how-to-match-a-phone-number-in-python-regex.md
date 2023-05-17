# How to match a phone number in Python regex?
// plain

The following regex can be used to match a phone number in Python:

```
\d{3}-\d{3}-\d{4}
```

This regex will match a phone number in the format of `123-456-7890`. The `\d` part of the regex stands for a digit (0-9), and the `{3}` and `{4}` indicate that the preceding digit should appear 3 and 4 times respectively.

## Code explanation


- `\d`: Matches any digit (0-9)
- `{3}`: Indicates that the preceding digit should appear 3 times
- `{4}`: Indicates that the preceding digit should appear 4 times

## Helpful links

- [Python Regex Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python Regex Cheat Sheet](https://www.debuggex.com/cheatsheet/regex/python)

onelinerhub: [How to match a phone number in Python regex?](https://onelinerhub.com/python-regex/how-to-match-a-phone-number-in-python-regex)
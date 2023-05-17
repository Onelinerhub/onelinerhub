# How to match zero or one occurence in Python regex?
// plain

To match zero or one occurence in Python regex, the `?` operator can be used.

For example,
```
import re

string = "Hello World"

match = re.search(r"World?", string)

if match:
    print("Match found:", match.group())
else:
    print("No match")
```

## Output example

```
Match found: World
```

The `?` operator is used to match zero or one occurence of the preceding character or group. In the example above, the `?` operator is used to match zero or one occurence of the string `World`.

## Code explanation

- `?` operator: used to match zero or one occurence of the preceding character or group

## Helpful links
- [Python Regular Expression Quick Guide](https://www.rexegg.com/regex-quickstart.html)

onelinerhub: [How to match zero or one occurence in Python regex?](https://onelinerhub.com/python-regex/how-to-match-zero-or-one-occurence-in-python-regex)
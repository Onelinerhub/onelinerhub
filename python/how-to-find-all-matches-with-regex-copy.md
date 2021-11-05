# How to use regex

```python
import re
found = re.search('[0-9]', 'I was 10 when I was a child')
```

- `import re` - module to work with regular expressions
- `found` - will contain list of found matches
- `search` - find a match of a specified regex in a specified string
- `[0-9]` - example regular expression (matches all difits)
- `I was 10 when I was a child` - example string to extract matches from

group: regex

## Example: 
```python
import re

found = re.search('[0-9]+', 'I was 10 when I was not 9')

print(found[0])
```
```
10

```

## Additional keywords
- regular expressions
- match

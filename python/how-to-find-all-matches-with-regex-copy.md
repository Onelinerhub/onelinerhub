# How to find all matches with regex COPY

```python
import re
found = re.findall('[0-9]', 'I was 10 when I was a child')
```

- `import re` - module to work with regular expressions
- `found` - will contain list of found matches
- `findall` - returns all found matches
- `[0-9]` - example regular expression (matches all difits)
- `I was 10 when I was a child` - example string to extract matches from

group: regex

## Example: 
```python
import re

found = re.findall('[0-9]+', 'I was 10 when I was not 9')

print(found)
```
```
['10', '9']

```

## Additional keywords
- regular expressions
- match

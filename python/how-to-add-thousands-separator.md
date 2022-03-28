# Add thousands separator to number

You could use the standard [format function](https://docs.python.org/3/library/string.html) to add separator based on local format:

```python
"{:,}".format(123456789)
# '123,456,789'
```

Or use re module for adding a custom separator to a number:
```python
import re

def add_thousand_separator(value : int, separator : str) -> str:
    """
    - value - number to be processed
    - separator - separator character, it can be comma (,) or period (.) based on local format
    """
    return re.sub(r"\B(?=(?:\d{3})+$)", separator, str(value))

add_thousand_separator(123456789, '-')
# '123-456-789'


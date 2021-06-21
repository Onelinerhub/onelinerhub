# Add thousands separator to number

```python
import re
re.sub(r"\B(?=(?:\d{3})+$)", separator, str(value))
```

- separator - separator character, it can be comma (,) or period (.) based on local format.
- value - number to be processed

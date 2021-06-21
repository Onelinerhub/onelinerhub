
# Transform camel case to snake case

```python
import re
re.sub('([a-z0-9])([A-Z])', r'\1_\2', value).lower()
```

- value - text to be processed, must be in string format.

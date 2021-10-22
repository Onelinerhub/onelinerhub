# How to format datetime

```python
from datetime import datetime
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

- `datetime` - python module to manipulate time
- `now()` - return current time
- `strftime` - method formats given time in a [specified format[(https://manpages.debian.org/bullseye/manpages-dev/strftime.3.en.html)

## Example: 
```python
from datetime import datetime
formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```
```
2023-10-22 16:19:53
```

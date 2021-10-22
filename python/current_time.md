# How to get current time

```python
from datetime import datetime
time = datetime.now().time()
```

- datetime - imported datetime class from the datetime module
- now().time() -  get a datetime object containing current time

group: date_time

## Example
```python
from datetime import datetime
time = datetime.now().time()
print(time)
```
```
16:16:25.981142
```

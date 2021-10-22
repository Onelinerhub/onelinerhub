# How to format datetime

```python
from datetime import datetime
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```


## Example: 
```python
from datetime import datetime
formatted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```
```
2023-10-22 16:19:53
```

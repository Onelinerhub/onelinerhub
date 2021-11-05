# How to get yesterday's date

```python
from datetime import datetime, timedelta
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
```


## Example: 
```python
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

print(datetime.now().strftime('%Y-%m-%d')) # today
print(yesterday)
```
```
2021-11-05
2021-11-04

```

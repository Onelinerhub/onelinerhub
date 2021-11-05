# How to get yesterday's date

```python
from datetime import datetime, timedelta
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
```

- `datetime` - module to manipulate dates and times
- `timedelta` - module to add/subtract dates
- `yesterday` - will store yesterdays date string in YYYY-MM-DD format
- `datetime.now()` - current datetime
- `timedelta(1)` - returns 1 day time delta (to subtract from today's date) 
- `strftime` - transform datetime to a string in a given format

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

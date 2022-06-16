# How to get first row from data frame

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

first = data.loc[0]
```


group: fetch

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

first = data.loc[0]
print(first)
```


# How to find mean of two dataframe columns

```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

res = data[['Price', 'Used']].mean()
```


group: mean

## Example: 
```python
import pandas as pd

data = pd.DataFrame({
  'Vendor': ['US', 'US', 'US', 'KR', 'KR'],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 102, 405, 350],
  'Used': [150, 250, 80, 320, 280]
})

res = data[['Price', 'Used']].mean()
print(res)
```
```
Price    273.0
Used     216.0
dtype: float64

```


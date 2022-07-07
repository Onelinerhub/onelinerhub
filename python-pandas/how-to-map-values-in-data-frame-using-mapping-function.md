# How to map values in data frame using mapping function

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

titles = {'ip5': 'Iphone 5', 'ip8' => 'Iphone 8'}

df['Phone'].map(titles)

print(df)
```


## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

titles = {'ip5': 'Iphone 5', 'ip8' => 'Iphone 8'}

df = df['Phone'].map(titles)

print(df)
```


# Select rows between two values in data frame

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[(df['price'] > 300) & (df['price'] < 400)]
```


group: query

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 304, 404, 405, 305]
})

found = df[(df['price'] > 300) & (df['price'] < 400)]
print(found)
```


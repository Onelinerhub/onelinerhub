# How to join data frames

```python
import pandas as pd

df1 = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305]
})

df2 = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Color': ['red', 'black', 'red', 'red', 'black']
})
```


group: join

## Example: 
```python
import pandas as pd

df1 = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305]
})

df2 = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Color': ['red', 'black', 'red', 'red', 'black']
})
```


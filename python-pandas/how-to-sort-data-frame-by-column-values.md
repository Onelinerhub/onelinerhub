# How to sort data frame by column values

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

df.sort_values(by=['price'])
```


group: sort

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

df = df.sort_values(by=['price'])
print(df)
```
```
  phone  price
0   ip5    204
4    xi    305
2   ip8    404
3   sms    405
1   ip6    704

```


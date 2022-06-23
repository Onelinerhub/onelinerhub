# How to sort data frame by multiple columns

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 405, 405, 305],
  'bonus': [10,15,20,50,20]
})

df.sort_values(by=['price', 'bonus'])
```


group: sort

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305],
  'bonus': [10,15,20,50,20]
})

df.sort_values(by=['price', 'bonus'])
print(df)
```
```
  phone  price  bonus
0   ip5    204     10
1   ip6    704     15
2   ip8    404     20
3   sms    405     50
4    xi    305     20

```


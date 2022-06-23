# How to sort dataframe by index

```python
# ...

df.sort_index()
```

- `df` - sample dataframe
- `sort_index()` - sorts given dataframe by index column

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

df = df.sort_index()
print(df)
```
```
  phone  price
0   ip5    204
4    xi    305
2   ip8    404
3   sms    405
1   ip6    704
  phone  price
0   ip5    204
1   ip6    704
2   ip8    404
3   sms    405
4    xi    305

```


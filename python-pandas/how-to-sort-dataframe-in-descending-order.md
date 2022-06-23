# How to sort dataframe in descending order

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

df = df.sort_values(by=['price'], ascending=False)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `sort_values` - sorts dataframe by column values
- `by=` - column names to sort by
- `'price'` - we're sorting by `price` column
- `ascending=False` - to sort in descending order

group: sort

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204, 704, 404, 405, 305]
})

df = df.sort_values(by=['price'], ascending=False)
print(df)
```
```
  phone  price
1   ip6    704
3   sms    405
2   ip8    404
4    xi    305
0   ip5    204

```


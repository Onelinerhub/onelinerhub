# How to join data frames

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305]
})

df_more = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Color': ['red', 'black', 'red', 'red', 'black']
})

df = df.join(df_more.set_index('Phone'), on='Phone')

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `df` - first data frame
- `df_more` - second data frame - the one to join to first
- `'Phone'` - column name to join dataframes by

group: join

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Price': [204, 304, 404, 405, 305]
})

df_more = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Color': ['red', 'black', 'red', 'red', 'black']
})

df = df.join(df_more.set_index('Phone'), on='Phone')

print(df)
```
```
  Phone  Price  Color
0   ip5    204    red
1   ip6    304  black
2   ip8    404    red
3   sms    405    red
4    xi    305  black

```


# How to map values in data frame using mapping function

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

titles = {'ip5': 'Iphone 5', 'ip8': 'Iphone 8'}
df['Titles'] = df['Phone'].map(titles)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `titles` - dict to use for mapping
- `'Phone'` - column to map values of
- `.map(` - maps values of a given column with values from specified dict
- `'Titles'` - column to write mapped values to

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

titles = {'ip5': 'Iphone 5', 'ip8': 'Iphone 8'}
df['Titles'] = df['Phone'].map(titles)

print(df)
```
```
  Phone  Phone Price    Titles
0   ip5          204  Iphone 5
1   ip6          304       NaN
2   ip8          404  Iphone 8
3   sms          405       NaN
4    xi          305       NaN

```


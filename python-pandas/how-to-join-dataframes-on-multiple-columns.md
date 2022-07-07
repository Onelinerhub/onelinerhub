# How to join dataframes on multiple columns

```python
import pandas as pd

df = pd.DataFrame({
  'a': ['ip1', 'ip2', 'ip1', 'ip1', 'ip2'],
  'b': [1, 1, 2, 3, 2],
  'c': [10, 11, 12, 13, 14]
})

df_more = pd.DataFrame({
  'a': ['ip1', 'ip2', 'ip2'],
  'b': [1, 1, 2],
  'd': ['s', 'e', 'y']
})

df = df.join(df_more.set_index(['a', 'b']), on=['a', 'b'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `df` - first data frame
- `df_more` - second data frame - the one to join to first
- `['a', 'b']` - columns list to join dataframes on

group: join

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'a': ['ip1', 'ip2', 'ip1', 'ip1', 'ip2'],
  'b': [1, 1, 2, 3, 2],
  'c': [10, 11, 12, 13, 14]
})

df_more = pd.DataFrame({
  'a': ['ip1', 'ip2', 'ip2'],
  'b': [1, 1, 2],
  'd': ['s', 'e', 'y']
})

df = df.join(df_more.set_index(['a', 'b']), on=['a', 'b'])
print(df)
```
```
     a  b   c    d
0  ip1  1  10    s
1  ip2  1  11    e
2  ip1  2  12  NaN
3  ip1  3  13  NaN
4  ip2  2  14    y

```


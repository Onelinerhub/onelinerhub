# What is opposite of melt() in Pandas

### Opposite of `melt()` method in Pandas is `pivot()`:

```python
import pandas as pd

# ...

df = melted_dataframe.pivot(index='Id',columns='variable',values='value')
print(df)

```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `melted_dataframe` - dataframe that was [previously melted](/python-pandas/how-to-use-melt-example) or is of similar "unvipot" structure
- `index='Id'` - index column to use
- `columns='variable'` - name of column to use as `variable` (property)
- `values='value'` - name of column to use as `value`

group: melt

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'Id':    [1, 10, 12, 15, 34],
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

melted = pd.melt(df, id_vars =['Id'], value_vars =['Phone', 'Phone Price'])
print(melted)

print()
df = melted.pivot(index='Id',columns='variable',values='value')
print(df)
```
```
   Id     variable value
0   1        Phone   ip5
1  10        Phone   ip6
2  12        Phone   ip8
3  15        Phone   sms
4  34        Phone    xi
5   1  Phone Price   204
6  10  Phone Price   304
7  12  Phone Price   404
8  15  Phone Price   405
9  34  Phone Price   305

variable Phone Phone Price
Id                        
1          ip5         204
10         ip6         304
12         ip8         404
15         sms         405
34          xi         305

```


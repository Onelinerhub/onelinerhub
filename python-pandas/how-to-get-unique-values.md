# How to get unique values from data frame

```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

uniq_vals = df.type.unique()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df.type` - address `type` column values
- `.unique()` - will return unique values for a specified column
- `uniq_vals` - will contain resulting array with unique values

group: unique

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

print(df.type.unique())
print(df.age.unique())
```
```
0    A
1    A
2    A
3    B
4    B
5    C
Name: type, dtype: object
['A' 'B' 'C']
[1 3 6 4]

```


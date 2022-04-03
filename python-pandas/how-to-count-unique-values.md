# How to count unique values

```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

uniq_count = df.type.unique().size
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `df.type` - address `type` column values
- `.unique()` - will return unique values for a specified column
- `.size` - return length of a given array
- `uniq_count` - will contain unique values size

group: unique

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

print(df.type.unique().size)
```
```
3

```


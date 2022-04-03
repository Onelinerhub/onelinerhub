# How to create pivot table from data frame

```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

pvt = pd.pivot_table(df , index=['type'], aggfunc=['max'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `pd.pivot_table` - creates [pivot table](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html) from given DataFrame and configuration
- `index=` - defines list of columns to use as pivot indexes (rows)
- `aggfunc=` - defines aggregate functions to use for column values

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  'type': ['A', 'A', 'A', 'B', 'B', 'C'],
  'age': [1, 3, 6, 3, 4, 1]
})

pvt = pd.pivot_table(df , index=['type'], aggfunc=['max'])
print(pvt)
```
```
     max
     age
type    
A      6
B      4
C      1

```


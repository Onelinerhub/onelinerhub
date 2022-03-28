# How to convert series to list

```python
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
lst = pd.Series.tolist(series)
```

- `pd.Series` - creates Pnada series
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.Series.tolist` - converts given Series object to list

group: series

## Example: 
```python
import pandas as pd
series = pd.Series([1, 2, 3, 4, 5])
lst = pd.Series.tolist(series)
print(lst)
```
```
[1, 2, 3, 4, 5]
```


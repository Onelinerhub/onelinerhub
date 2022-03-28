# How to convert list to Pandas Series

```python
import pandas as pd
lst = [1, 2, 3, 4, 5]
series = pd.Series(lst)
```

- `pd.Series` - creates Panda series from given list
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)

group: series

## Example: 
```python
import pandas as pd
lst = [1, 2, 3, 4, 5]
series = pd.Series(lst)
print(series)
```
```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```


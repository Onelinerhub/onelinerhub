# How to floor values in dataframe

```python
import pandas as pd

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204.10, 304.99, 404.5, 405.5, 305.90]
})

df['price'] = df['price'].apply(np.floor)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.apply(` - applies given callback to all values of given column (or multiple columns)
- `np.floor` - [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) floor function

group: rounding

## Example: 
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
  'phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'price': [204.10, 304.99, 404.5, 405.5, 305.90]
})

df['price'] = df['price'].apply(np.floor)
print(df)
```
```
  phone  price
0   ip5  204.0
1   ip6  304.0
2   ip8  404.0
3   sms  405.0
4    xi  305.0

```


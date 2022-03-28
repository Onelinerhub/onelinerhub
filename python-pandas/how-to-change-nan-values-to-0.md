# How to change nan values to zero

```python
import pandas as pd
import numpy as np

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, np.nan, 78, np.nan],
  'Phone Price': [204, np.nan, 501, 800, np.nan]
}

data = pd.DataFrame(phoneDataSet)
data = data.replace(np.nan, 0)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `phoneDataSet` - sample dict data to create dataframe from
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.replace(` - search given value and replace with specified value 
- `np.nan` - value to search for

group: nan

## Example: 
```python
import pandas as pd
import numpy as np

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, np.nan, 78, np.nan],
  'Phone Price': [204, np.nan, 501, 800, np.nan]
}

data = pd.DataFrame(phoneDataSet)
data = data.replace(np.nan, 0)

print(data)
```
```
            Phone  Phone ID.  Phone Price
0        iPhone 5       12.0        204.0
1        iPhone 6        9.0          0.0
2         iPhone8        0.0        501.0
3       Galaxy S9       78.0        800.0
4  Galaxy Note 10        0.0          0.0

```


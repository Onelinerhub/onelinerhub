# Get moving average for Numpy array

```python
import pandas as pd
import numpy as np

data = np.array([1,1,2,3,4,5,3,3,6,6])
d = pd.Series(data)

ma = d.rolling(3).mean()
```

- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `np.array` - declare Numpy array
- `pd.Series` - create [Pandas](/python-pandas) series
- `.rolling(3)` - get rolling window object with a specified size (3 elements in our case)
- `.mean()` - calculates moving average
- `ma` - will contain [Pandas](/python-pandas) series with moving averages

## Example: 
```python
import pandas as pd
import numpy as np

data = np.array([1,1,2,3,4,5,3,3,6,6])
d = pd.Series(data)

print(d.rolling(3).mean())
```
```
Rolling [window=3,center=False,axis=0,method=single]
0         NaN
1         NaN
2    1.333333
3    2.000000
4    3.000000
5    4.000000
6    4.000000
7    3.666667
8    4.000000
9    5.000000
dtype: float64

```


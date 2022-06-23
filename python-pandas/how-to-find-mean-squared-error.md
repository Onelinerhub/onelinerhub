# How to find mean squared error

```python
import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.DataFrame({
  'y1': [200, 310, 404, 400, 200],
  'y2': [204, 304, 404, 405, 204]
})

mse = mean_squared_error(df['y1'], df['y2'])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `sklearn` - load [lib:Scikit-learn module](/python-pandas/how-to-find-mean-squared-error) to work with science stuff
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `mean_squared_error(` - calculates mean squared error (`MSE`) between 2 set of values
- `df['y1'], df['y2']` - two column values to calculate `MSE` for

## Example: 
```python
import pandas as pd
from sklearn.metrics import mean_squared_error

df = pd.DataFrame({
  'y1': [200, 310, 404, 400, 200],
  'y2': [204, 304, 404, 405, 204]
})

mse = mean_squared_error(df['y1'], df['y2'])
print(mse)
```
```
18.6

```


# Use imputer for one column only

```python
import numpy as np
import pandas as pd
from sklearn import impute

im = impute.SimpleImputer(missing_values=np.nan, strategy='mean')

df = pd.DataFrame([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]], columns=['A', 'B', 'C'])
df['B'] = im.fit_transform(df[['B']])
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `.SimpleImputer(` - univariate imputer for completing missing values with simple strategies.
- `df[['B']]` - impute values for `B` column only

group: impute

## Example: 
```python
import numpy as np
import pandas as pd
from sklearn import impute

im = impute.SimpleImputer(missing_values=np.nan, strategy='mean')

df = pd.DataFrame([[7, 2, 3], [4, np.nan, 6], [10, 5, 9]], columns=['A', 'B', 'C'])
df['B'] = im.fit_transform(df[['B']])

print(df)
```
```
    A    B  C
0   7  2.0  3
1   4  3.5  6
2  10  5.0  9

```


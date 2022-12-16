# Simple imputer example

```python
import numpy as np
from sklearn import impute

im = impute.SimpleImputer(missing_values=np.nan, strategy='mean')

X = [[7, 2, 3], [4, np.nan, 6], [10, 5, 9]]
Xi = im.fit_transform(X)
```

- `from sklearn import` - import module from [lib:scikit-learn](https://onelinerhub.com/python-scikit-learn/how-to-install-scikit-learn-using-pip)
- `import numpy` - import [lib:Numpy](https://onelinerhub.com/python-numpy/how-to-install-python-numpy-lib) module
- `.SimpleImputer(` - univariate imputer for completing missing values with simple strategies.
- `missing_values` - which values to treat as missing
- `strategy` - select strategy for filling missing values
- `.fit_transform(` - trains and transforms given data with missing values filled

group: impute

## Example: 
```python
import numpy as np
from sklearn import impute

im = impute.SimpleImputer(missing_values=np.nan, strategy='mean')

X = [[7, 2, 3], [4, np.nan, 6], [10, 5, 9]]
Xi = im.fit_transform(X)

print(Xi)
```
```
[[ 7.   2.   3. ]
 [ 4.   3.5  6. ]
 [10.   5.   9. ]]

```


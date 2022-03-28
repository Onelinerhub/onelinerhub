# How to change nan values to 0

```python
import pandas as pd
import numpy as np

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, np.nan, 78, 1, np.nan],
  'Phone Price': [204, np.nan, 501, 800, np.nan]
}

data = pd.DataFrame(phoneDataSet)
data = data.replace(np.nan, 0)
print(data)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python

group: nan

## Example: 
```python
import pandas as pd
import numpy as np

phoneDataSet = {
  'Phone': ['iPhone 5', 'iPhone 6', 'iPhone8', 'Galaxy S9', 'Galaxy Note 10'],
  'Phone ID.': [12, 9, np.nan, 78, 1, np.nan],
  'Phone Price': [204, np.nan, 501, 800, np.nan]
}

data = pd.DataFrame(phoneDataSet)
data = data.replace(np.nan, 0)
print(data)
```


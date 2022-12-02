# Load Boston housing dataset

```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_boston(return_X_y=True)
```


group: datasets

## Example: 
```python
import numpy as np
from sklearn import datasets

X, y = datasets.load_boston(return_X_y=True)

print(X.shape)
print(y.shape)
```


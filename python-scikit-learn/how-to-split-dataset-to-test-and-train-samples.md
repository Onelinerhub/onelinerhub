# How to split dataset to test and train samples

```python
import numpy as np
from sklearn import datasets, model_selection

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)
```


## Example: 
```python
import numpy as np
from sklearn import datasets, model_selection

X, y = datasets.load_diabetes(return_X_y=True)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)
```


# How to plot data frame

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = {'a': np.random.normal(0,1,100), 'b' : np.random.normal(1,2,100)}
df = pd.DataFrame.from_dict(a)

df.plot()
plt.show()
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `import numpy as np` - load [lib:Numpy module](/python-numpy/how-to-install-python-numpy-lib) for Python
- `.random.normal(0,1,100)` - generates `100` elements with `0` mean and `1` standard deviation
- `.DataFrame.from_dict` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) from given dict (`a`)
- `.plot()` - plots DataFrame
- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `plt.show()` - renders plotted data

group: charts

## Example: 
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = {'a': np.random.normal(0,1,100), 'b' : np.random.normal(1,2,100)}
df = pd.DataFrame.from_dict(a)

df.plot()
plt.show()
```


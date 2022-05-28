# How to make bar chart from Pandas Dataframe

```python
import matplotlib.pyplot as plt
import pandas as pd

data = {
  'iPhone.': [12, 900, 78],
  'Android': [204, 501, 800]
}

df = pd.DataFrame(data, index = ['some', 'metric', 'other'])

df.plot.bar()

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `data = {` - define data for data frame
- `pd.DataFrame` - create [Pandas Dataframe](/python-pandas/example-of-using-python-pandas) from specified data
- `index =` - specify column names
- `plot.bar()` - will plot Dataframe data as bar charts
- `.show()` - render chart in a separate window

group: bar

## Example: 
```python
import matplotlib.pyplot as plt
import pandas as pd

data = {
  'iPhone.': [12, 900, 78],
  'Android': [204, 501, 800]
}

df = pd.DataFrame(data, index = ['some', 'metric', 'other'])

df.plot.bar()

plt.show()
```


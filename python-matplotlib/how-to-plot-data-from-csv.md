# How to plot data from CSV

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/var/www/examples/data.csv")
plt.plot(df.a, df.b)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.read_csv` - read specified `CSV` file
- `/var/www/examples/data.csv` - path to sample `CSV` file
- `.plot(` - plot specified data
- `df.a, df.b` - use column `a` data for `X` axis and `b` column data for `Y` axis
- `.show()` - render chart in a separate window

group: from

## Example: 
```python
import pandas as pd
import matplotlib.pyplot as plt

with open('/var/www/examples/data.csv', 'r') as f:
  print(f.read()) # print CSV file contents

df = pd.read_csv("/var/www/examples/data.csv")

plt.plot(df.a, df.b)
plt.show()
```
```
a,b
1,4
2,3
3,6


```


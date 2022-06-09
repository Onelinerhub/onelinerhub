# How to plot data from csv

```python
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["a", "b", "c"]
df = pd.read_csv("/var/www/examples/file.csv", usecols=columns)
plt.plot(df.Name, df.Marks)
plt.show()
```


## Example: 
```python
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["a", "b", "c"]
df = pd.read_csv("/var/www/examples/file.csv", usecols=columns)
plt.plot(df.Name, df.Marks)
plt.show()
```


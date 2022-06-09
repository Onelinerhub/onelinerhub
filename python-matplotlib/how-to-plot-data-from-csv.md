# How to plot data from csv

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/var/www/examples/data.csv")
plt.plot(df.a, df.b)
plt.show()
```


## Example: 
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/var/www/examples/data.csv")

plt.plot(df.a, df.b)
plt.show()
```


# How to plot data from JSON

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/var/www/examples/data.csv")
plt.plot(df.a, df.b)
plt.show()
```


group: from



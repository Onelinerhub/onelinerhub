# How to plot datetime for x axis

```python
import matplotlib.pyplot as plt
import datetime

x = [datetime.datetime(2022,10,11), datetime.datetime(2022,10,12), datetime.datetime(2022,10,13)]
plt.plot(x, [5,12,43])

plt.show()
```


## Example: 
```python
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

x = [datetime.datetime(2022,10,11), datetime.datetime(2022,10,12), datetime.datetime(2022,10,13)]
plt.plot(x, [5,12,43])

# plt.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.show()
```


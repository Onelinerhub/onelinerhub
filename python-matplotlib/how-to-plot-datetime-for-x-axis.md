# How to plot datetime for x axis

```python
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

fig, ax = plt.subplots()

x = [datetime.datetime(2022,10,11), datetime.datetime(2022,10,12), datetime.datetime(2022,10,13)]
ax.plot(x, [5,12,43])

ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.subplots(` - creates set of charts on a single chart area
- `datetime.datetime(` - created date object
- `.plot(` - plot specified data
- `mdates.DayLocator(interval=1)` - we want to label `X` axis ticks every day 
- `mdates.DateFormatter('%m/%d')` - we want to format `X` axis ticks labels as `mm/dd`
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

fig, ax = plt.subplots()

x = [datetime.datetime(2022,10,11), datetime.datetime(2022,10,12), datetime.datetime(2022,10,13)]
ax.plot(x, [5,12,43])

ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))

plt.show()
```


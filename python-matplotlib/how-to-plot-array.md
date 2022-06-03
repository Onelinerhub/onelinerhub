# How to plot array

### We can pass array directly to `plot()` method to plot its values:

```python
import matplotlib.pyplot as plt

data = [2,3,5,1,1,3,6,7,2,2,1,4,5,6]

plt.plot(data)

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `data =` - declare sample array to plot
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt

data = [2,3,5,1,1,3,6,7,2,2,1,4,5,6]

plt.plot(data)

plt.show()
```


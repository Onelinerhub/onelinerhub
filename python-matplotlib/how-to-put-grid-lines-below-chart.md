# How to put grid lines below chart

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4,2,5,1,7,3,4])
plt.yscale('log')
plt.grid(b=True, which='major', color='#444',linestyle='--')
plt.grid(b=True, which='minor', color='#ccc',linestyle='--')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.grid(` - add and configure grid
- `which` - specify which grid type to configure (`major` or `minor`)
- `color` - grid line color
- `linestyle` - grid line style
- `.show()` - render chart in a separate window

group: grid

## Example: 
```python
import matplotlib.pyplot as plt
plt.bar(['UA', 'UK', 'USA'], [10, 11, 12])
plt.grid()
plt.show()
```


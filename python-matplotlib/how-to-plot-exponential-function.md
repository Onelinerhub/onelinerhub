# How to plot exponential function

```python
import matplotlib.pyplot as plt
plt.plot([1,2**2,3**3,4**4,5**5,6**6,7**7])
plt.yscale('log')
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `.yscale('log')` - scale `Y` axis exponentially
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2**2,3**3,4**4,5**5,6**6,7**7])
plt.yscale('log')
plt.show()
```


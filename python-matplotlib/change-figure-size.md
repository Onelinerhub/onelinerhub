# How to change figure size

```python
import matplotlib.pyplot as plt
plt.figure(figsize=(2, 2), dpi=80)
plt.plot([4,2,11,2,1,20,25])
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.figure(` - change figure params
- `figsize` - set figure size in inches
- `dpi` - inch size in pixels (`80` in our case)
- `.plot(` - plot specified data
- `.show()` - render chart in a separate window

group: figure

## Example: 
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(2, 2), dpi=80)
plt.plot([4,2,11,2,1,20,25])
plt.show()
```


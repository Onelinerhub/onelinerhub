# How to only save image

```python
import matplotlib.pyplot as plt
plt.plot([1,3,2])
plt.savefig('plot.png')
plt.close()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `savefig(` - saves chart to the specified image file
- `plot.png` - image file to save chart to
- `.close()` - we don't want to do anything else

group: image



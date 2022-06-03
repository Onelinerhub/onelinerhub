# How to set image size

### In order to set exported image size, we need to modify `dpi` param to configure resolution in pixels per inch:

```python
import matplotlib.pyplot as plt
plt.plot([1,3,2])
plt.savefig('plot.png', dpi=500)
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `savefig(` - saves chart to the specified image file
- `plot.png` - image file to save chart to
- `dpi=` - modify image size by setting dots per inch

group: image



# How to add axis label

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `mpl.rc` - manage configuration
- `'axes', labelcolor` - axes labels color
- `.show()` - render chart in a separate window

group: label

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
```


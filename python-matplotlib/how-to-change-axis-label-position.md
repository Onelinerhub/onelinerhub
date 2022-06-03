# How to change axis label position

```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel("X title", loc="right")
plt.ylabel("Y title", loc="top")

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `xlabel` - set label for x-axis
- `ylabel` - set label for y-axis
- `loc=` - set label position
- `.show()` - render chart in a separate window

group: label

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,1,3])
plt.xlabel("X title", loc="right")
plt.ylabel("Y title", loc="top")

plt.show()
```


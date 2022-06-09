# How to draw a vector

```python
import matplotlib.pyplot as plt
plt.quiver(0.1,0.2,scale=1)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.quiver(` - plots arrow(s)
- `0.1,0.2` - arrow direction
- `scale=1` - set arrow length
- `.show()` - render chart in a separate window

group: vector

## Example: 
```python
import matplotlib.pyplot as plt
plt.quiver(0.1,0.2,scale=1)
plt.show()
```


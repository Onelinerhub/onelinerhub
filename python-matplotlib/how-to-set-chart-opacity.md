# How to set chart opacity

### Pass `alpha` argument to set level of chart transparency:

```python
import matplotlib.pyplot as plt

plt.plot([2,5,1,4,6,7], alpha=0.3)
plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `.plot(` - plot specified data
- `alpha` - sets level of transparency
- `0.3` - set transparency level to 30% 
- `.show()` - render chart in a separate window

## Example: 
```python
import matplotlib.pyplot as plt

plt.plot([2,5,1,4,6,7], alpha=0.3)
plt.show()
```


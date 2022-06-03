# How to set image size

### In order to set exported image size, we need to modify `dpi` param to configure resolution in pixels per inch:

```python
import matplotlib.pyplot as plt
plt.plot([1,3,2])
plt.savefig('plot.png', dpi=500)
```


group: image



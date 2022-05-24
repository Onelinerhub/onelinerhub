# How to set background transparency

```python
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('cyan')
plt.axes().set_facecolor('black')
plt.plot([2,1,2,2])
plt.show()
```


group: background

## Example: 
```python
import matplotlib.pyplot as plt
plt.figure().patch.set_facecolor('cyan')
plt.axes().set_facecolor('black')
plt.axes().set_alpha(0.5)
plt.plot([2,1,2,2])
plt.show()
```


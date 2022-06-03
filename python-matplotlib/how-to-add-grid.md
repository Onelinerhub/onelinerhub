# How to add grid

```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.legend()
plt.show()
```


group: grid

## Example: 
```python
import matplotlib.pyplot as plt
plt.plot([1,2,10,6,15,3,4], label='A')
plt.plot([4,2,11,2,1,20,25], label='B')
plt.grid(True)
plt.show()
```


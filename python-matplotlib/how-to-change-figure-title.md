# How to change figure title

```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)
axs[0].plot([2,1,5,2,3])
axs[0].set_title('first line')

fig.suptitle('I am figure title')

axs[1].plot([4,2,4,6,1])
axs[1].set_title('second line')

plt.show()
```


group: figure

## Example: 
```python
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1)
axs[0].plot([2,1,5,2,3])
axs[0].set_title('first line')

fig.suptitle('I am figure title')

axs[1].plot([4,2,4,6,1])
axs[1].set_title('second line')

plt.show()
```


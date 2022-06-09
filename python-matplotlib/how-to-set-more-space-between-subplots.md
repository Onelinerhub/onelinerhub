# How to set more space between subplots

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4,2))

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])

plt.show()
```


group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(4,2))

axes[0].plot([1,3,2])
axes[1].plot([8,2,5])

plt.show()
```


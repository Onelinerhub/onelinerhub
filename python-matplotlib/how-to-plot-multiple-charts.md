# How to plot multiple charts

```python
# Import library

import matplotlib.pyplot as plt

# Create figure


fig = plt.figure()

# Create each subplot individually


ax1 = plt.subplot(131)
ax2 = plt.subplot(132)
ax3 = plt.subplot(133)

# Auto adjust


plt.tight_layout()

# Display

plt.show()
```


group: multiple

## Example: 
```python
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = plt.subplot(131)
ax2 = plt.subplot(132)
ax3 = plt.subplot(133)

plt.tight_layout()

plt.show()
```


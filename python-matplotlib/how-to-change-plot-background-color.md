# How to change plot background color

```bash
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.show()
```


group: background

## Example: 
```bash
import matplotlib.pyplot as plt
plt.plot([2,1,2,2])
fig = plt.figure()
fig.patch.set_facecolor('green')
plt.show()
```


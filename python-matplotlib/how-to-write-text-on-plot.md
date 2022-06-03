# How to write text on plot

```python
import matplotlib.pyplot as plt

fig, axe = plt.subplots()
axe.plot([2,1,3,6,2])
axe.text(-2.5, 0.5, "hi from python", bbox=dict(facecolor='red', alpha=0.5))

plt.show()
```




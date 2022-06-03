# How to write text on plot

```python
import matplotlib.pyplot as plt

fig, axe = plt.subplots()
axe.plot([2,1,3,6,2])
axe.text(1, 3.5, "hi from python")

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities

## Example: 
```python
import matplotlib.pyplot as plt

fig, axe = plt.subplots()
plt.plot([2,1,3,6,2])
plt.text(1, 3.5, "hi from python")

plt.show()
```


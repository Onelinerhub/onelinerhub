# How to set table row height

```python
import matplotlib.pyplot as plt

data = [[1, 2, 3, 4, 5],
        [10,20,30,40,50],
        [11,21,31,41,51]]

plt.table(data, loc='center', colLabels=['A','B','C','D','E'])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `data =` - data to use for table cells
- `.table(` - plot a table from specified data
- `loc='center'` - position table in the middle of the chart area 
- `colLabels` - list of column titles

group: table

## Example: 
```python
import matplotlib.pyplot as plt

data = [[1, 2, 3, 4, 5],
        [10,20,30,40,50],
        [11,21,31,41,51]]

t = plt.table(data, loc='center', colLabels=['A', 'B', 'C', 'D', 'E'])
t.scale(1, 4)

plt.show()
```


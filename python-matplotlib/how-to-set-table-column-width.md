# How to change table column width

```python
import matplotlib.pyplot as plt

data = [[1, 2, 3, 4, 5],
        [10,20,30,40,50],
        [11,21,31,41,51]]

plt.table(data, loc='center', colWidths=[.2,.1,.1,.1,.1])

plt.show()
```

- `import matplotlib.pyplot as plt` - loads [lib:Matplotlib module](python-matplotlib/how-to-install-matplotlib-python-lib-in-ubuntu-ubuntuversion) to use plotting capabilities
- `data =` - data to use for table cells
- `.table(` - plot a table from specified data
- `loc='center'` - position table in the middle of the chart area 
- `colWidths` - set width of columns based on the list of given values (relative to the chart area, where `1` is 100% of chart area)
- `.2` - set first column width to 20% of chart area
- `.1` - set other columns width to 10% of chart area

group: table

## Example: 
```python
import matplotlib.pyplot as plt

data = [[1, 2, 3, 4, 5],
        [10,20,30,40,50],
        [11,21,31,41,51]]

plt.table(data, loc='center', colWidths=[.2,.1,.1,.1,.1])

plt.show()
```


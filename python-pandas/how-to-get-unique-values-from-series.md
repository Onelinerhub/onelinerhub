# How to get unique values from series

```python
import pandas as pd

my_list = [10, 100, 100, 10, 1, 1000]
my_series = pd.Series(my_list)

uniq_vals = pd.unique(my_series)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `my_list` - declare a python list and assign values
- `pd.Series(my_list)` - constructing a Series using pandas
- `pd.unique(` - returns unique values of specified Series

group: unique

## Example: 
```python
import pandas as pd

my_list = [10, 100, 100, 10, 1, 1000]
my_serie = pd.Series(my_list)

print("My serie")
print(my_serie)

print("Unique values:")
print(pd.unique(my_serie))
```
```
My serie
0      10
1     100
2     100
3      10
4       1
5    1000
dtype: int64
Unique values:
[  10  100    1 1000]

```


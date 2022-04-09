# How to load data frame from CSV

```python
import pandas as pd

f = open('/var/www/examples/file.csv')
data = pd.read_csv(f)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `open(` - opens specified file for reading
- `/var/www/examples/file.csv` - path to CSV file to read
- `pd.read_csv(` - loads data frame from specified `CSV` file 
- `data` - will contain loaded DataFrame

group: csv

## Example: 
```python
import pandas as pd

f = open('/var/www/examples/file.csv')
data = pd.read_csv(f)

print(data)
print(type(data))
```
```
   a  b  c
0  1  2  3
1  1  3  5
<class 'pandas.core.frame.DataFrame'>

```


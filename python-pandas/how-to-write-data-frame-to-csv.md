# How to write data frame to CSV

```python
import pandas as pd

df = pd.DataFrame(
  {
    "A": 1.0,
    "B": pd.Timestamp("20220102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "E": pd.Categorical(["test", "first", "test", "second"]),
    "F": "foo"
  }
)

df.to_csv('/tmp/data.csv')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `.to_csv` - saves DataFrame to the specified `CSV` file
- `/tmp/data.csv` - path to `CSV` file to save data to 

group: csv

## Example: 
```python
import pandas as pd

df = pd.DataFrame(
  {
    "A": 1.0,
    "B": pd.Timestamp("20220102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "E": pd.Categorical(["test", "first", "test", "second"]),
    "F": "foo"
  }
)

df.to_csv('/tmp/data.csv')

with open('/tmp/data.csv', 'r') as f:
  print(f.read())
```
```
,A,B,C,E,F
0,1.0,2022-01-02,1.0,test,foo
1,1.0,2022-01-02,1.0,first,foo
2,1.0,2022-01-02,1.0,test,foo
3,1.0,2022-01-02,1.0,second,foo


```


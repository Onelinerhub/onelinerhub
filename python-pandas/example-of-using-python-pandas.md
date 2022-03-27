# Example of using Python Pandas

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

print(df[df['E']=="test"])
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `pd.Timestamp` - generates timestamp object from given date
- `pd.Series` - generates series of given values and given type
- `pd.Categorical` - generates list of categorical data (e.g. text name of category)
- `df[df['E']=="test"]` - pick only those `df` rows which has `E` column values equal to `test`

group: quickstart

## Example: 
```python
import pandas as pd

df = pd.DataFrame(
  {
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "E": pd.Categorical(["test", "first", "test", "second"]),
    "F": "foo"
  }
)

print(df[df['E']=="test"])
```
```
     A          B    C     E    F
0  1.0 2022-01-02  1.0  test  foo
2  1.0 2022-01-02  1.0  test  foo
```


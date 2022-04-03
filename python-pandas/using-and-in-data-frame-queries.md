# Using AND in data frame queries

```python
import pandas as pd

df = pd.DataFrame({
  "Brand": ["Ford", "BMW", "Lexus"],
  "Color": ["Silver", "Black", "Silver"],
  "Model": ["F-2020", "B-2021", "L-2020"]
})

ford_and_silver = df[(df["Brand"] == "Ford") & (df["Color"] == "Silver")]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `ford_and_silver` - resulting data DataFrame all cars that are both `Ford` **and** `Silver`
- `df["Brand"] == "Ford"` - Mask of all cars whose `Brand` equals `Ford`
- `df["Color"] == "Silver"` - Mask of all cars whose `Color` equals `Silver`
- `&` - Boolean `AND` operator

group: and_or

## Example: 
```python
import pandas as pd

df = pd.DataFrame({
  "Brand": ["Ford", "BMW", "Lexus"],
  "Color": ["Silver", "Black", "Silver"],
  "Model": ["F-2020", "B-2021", "L-2020"]
})

ford_and_silver = df[(df["Brand"] == "Ford") & (df["Color"] == "Silver")]
print(ford_and_silver)
```
```
  Brand   Color   Model
0  Ford  Silver  F-2020

```


# Using OR in data frame queries

```python
import pandas as pd

df = pd.DataFrame({
  "Brand": ["Ford", "BMW", "Lexus"],
  "Color": ["Silver", "Black", "Silver"],
  "Model": ["F-2020", "B-2021", "L-2020"]
})

ford_or_lexus = df[(df["Brand"] == "Ford") | (df["Brand"] == "Lexus")]
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `pd.DataFrame` - creates Pandas [DataFrame object](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- `ford_or_lexus` - resulting `DataFrame` containing all cars that are either `Ford` or `Lexus`
- `df["Brand"] == "Ford"` - Mask of all cars whose `Brand` equals `Ford`
- `df["Brand"] == "Lexus"` - Mask of all cars whose `Brand` equals `Lexus`
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

ford_or_lexus = df[(df["Brand"] == "Ford") | (df["Brand"] == "Lexus")]
print(ford_or_lexus)
```
```
   Brand   Color   Model
0   Ford  Silver  F-2020
2  Lexus  Silver  L-2020

```


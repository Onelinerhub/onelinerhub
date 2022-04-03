# Using and/or in queries

```python
import pandas

# Toy cars sample
df = pandas.DataFrame({
    "Brand": ["Ford", "BMW", "Lexus"],
    "Color": ["Silver", "Black", "Silver"],
    "Model": ["F-2020", "B-2021", "L-2020"]
})

# AND query
ford_and_silver = df[(df["Brand"] == "Ford") & (df["Color"] == "Silver")]
# OR query
ford_or_lexus = df[(df["Brand"] == "Ford") | (df["Brand"] == "Lexus")]
```

- `import pandas` - Loads [lib:Pandas module](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html) for Python
- `df (pandas.DataFrame)` - Sample `DataFrame` containing cars, with their colors and models
- `ford_and_silver (pandas.DataFrame)` - `DataFrame` containing all cars that are both `Ford` **and** `Silver`
- `ford_or_lexus (pandas.DataFrame)` - `DataFrame` containing all cars that are either `Ford` **or** `Lexus`
- `df["Brand"] == "Ford" (pandas.Series)` - Mask of all cars whose `Brand` **equals** `Ford`
- `df["Color"] == "Silver" (pandas.Series)` - Mask of all cars whose `Color` **equals** `Silver`
- `df["Brand"] == "Lexus" (pandas.Series)` - Mask of all cars whose `Brand` **equals** `Lexus`
- `|` - Boolean `OR` operator
- `&` - Boolean `AND` operator

## Example:

```python
import pandas

df = pandas.DataFrame({
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


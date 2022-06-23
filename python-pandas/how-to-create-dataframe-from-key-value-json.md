# How to create dataframe from key-value JSON

```python
import pandas as pd
json = '''[{"Phone":"ip5","Price":100},{"Phone":"ip6","Price":150}]'''
df = pd.read_json(json)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `.read_json(` - will parse specified JSON string and create dataframe

group: json

## Example: 
```python
import pandas as pd
json = '''[{"Phone":"ip5","Price":100},{"Phone":"ip6","Price":150}]'''
df = pd.read_json(json)
print(df)
```
```
  Phone  Price
0   ip5    100
1   ip6    150

```


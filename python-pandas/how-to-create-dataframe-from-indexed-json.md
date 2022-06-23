# How to create dataframe from indexed JSON

```python
import pandas as pd
json = '''{"id1": {"Phone":"ip5","Price":100},"id2":{"Phone":"ip6","Price":150}}'''
df = pd.read_json(json, orient='index')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `.read_json(` - will parse specified JSON string and create dataframe
- `orient='index'` - ask Pandas to treat outer keys as indexes

group: json

## Example: 
```python
import pandas as pd
json = '''{"id1": {"Phone":"ip5","Price":100},"id2":{"Phone":"ip6","Price":150}}'''
df = pd.read_json(json, orient='index')
print(df)
```
```
    Phone  Price
id1   ip5    100
id2   ip6    150

```


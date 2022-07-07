# How to convert object values to string

```python
import pandas as pd

# df = pd.DataFrame({ ... })

df['col'] = df['col'].astype('|S')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `'col'` - column to convert to string
- `.astype(` - converts given column to specified type
- `'|S'` - string type

group: convert



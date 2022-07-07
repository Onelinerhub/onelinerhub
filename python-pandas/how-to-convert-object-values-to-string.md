# How to convert column values to Int

```python
import pandas as pd

# df = pd.DataFrame({ ... })

df['col'] = df['col'].astype(int)
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `'col'` - column to convert values of
- `.astype(` - converts given column to specified type
- `int` - Integer type

group: convert



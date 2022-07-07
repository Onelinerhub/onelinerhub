# How to write dataframe to Excel file (XSL)

### You might need to install [`openpyxl`](/python-pandas/how-to-install-openpyxl-module) module to work with Excel format:

```python
import pandas as pd

df = pd.DataFrame({
  'Phone': ['ip5', 'ip6', 'ip8', 'sms', 'xi'],
  'Phone Price': [204, 304, 404, 405, 305]
})

df.to_excel('/path/to/file.xlsx')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `to_excel` - saves dataframe to Excel file
- `/path/to/file.xlsx` - path to XLS file to save dataframe to

group: xls



# How to load dataframe from Excel (XSL)

### You might need to install [`openpyxl`](/python-pandas/how-to-install-openpyxl-module) module to work with Excel format:

```python
import pandas as pd

df = pd.read_excel('/path/to/data.xlsx')
```

- `import pandas as pd` - load [lib:Pandas module](/python-pandas/how-to-install-pandas)
- `read_excel` - reads dataframe from Excel file
- `/path/to/data.xlsx` - path to Excel file to read dataframe from

group: xls



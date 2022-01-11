# Combine 2 csv files using ID column

### We'll merge `data1.csv` and `data2.csv` into `output.csv`

```python
import pandas as pd
csv_1 = pd.read_csv('data1.csv')
csv_2 = pd.read_csv('data2.csv')
merged = csv_1.merge(csv_2, on='id')
merged.to_csv('output.csv', sep=',', header=True, index=False)
```

- `import pandas` - import module for converting, parsing and merging data
- `pd.read_csv` - reads CSV data from a given file
- `csv_1.merge` - merges CSV data with given data based on specified ID column
- `on='id'` - column name to merge data on
- `merged.to_csv` - save result to CSV file

group: combine_files



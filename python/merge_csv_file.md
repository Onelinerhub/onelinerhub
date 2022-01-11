# Combine Two .csv file with index column
```python
import pandas as pd
csv_1 = pd.read_csv('data1.csv')
csv_2 = pd.read_csv('data2.csv')
merged = csv_1.merge(csv_2, on='id')
merged.to_csv('output.csv', sep=',', header=True, index=False)
```

Combine the two .csv files with this code from index column
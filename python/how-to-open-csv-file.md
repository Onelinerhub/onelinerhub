# How to open CSV file

```python
import csv

with open('file.csv') as f:
  reader = csv.reader(f)

  for row in reader:
    print(row)
```

- `csv` - module to manipulate CSV
- `file.csv` - path to CSV file
- `csv.reader` - parses CSV from given file handler
- `for row in reader` - iterate through all rows in CSV

group: csv

## Example: 
```python
import csv

with open('/var/www/examples/file.csv') as f:
  reader = csv.reader(f)

  for row in reader:
    print(row)
```
```
['a', 'b', 'c']
['1', '2', '3']
['1', '3', '5']

```

## Additional keywords
- read
- parse

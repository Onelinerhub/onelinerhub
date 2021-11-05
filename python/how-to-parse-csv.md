# How to parse CSV

```python
from io import StringIO
import csv

reader = csv.reader(StringIO('some,csv,string'))

for row in reader:
  print(row)
```

- `StringIO` - creates IO handler from string
- `csv` - module to manipulate CSV
- `csv.reader` - parses CSV from given IO handler (string IO handler in our case)
- `some,csv,string` - example csv string
- `for row in reader` - iterate through each row in our CSV structure

group: csv

## Example: 
```python
from io import StringIO
import csv

string = '1,2,3,4';

reader = csv.reader(StringIO(string))

for row in reader:
  print(row)
```
```
['1', '2', '3', '4']

```

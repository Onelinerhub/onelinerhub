# x

How can I use Python and Numpy to read and write data from an XLSX file?
// plain

Python and Numpy can be used to read and write data from an XLSX file. To do this, the `openpyxl` library can be used. This library allows you to open and modify XLSX files in Python.

The following example shows how to read data from an XLSX file and write it to a Numpy array:

```python
import openpyxl
import numpy as np

# Open the XLSX file
wb = openpyxl.load_workbook('data.xlsx')

# Get the active sheet
ws = wb.active

# Read the data from the sheet into a Numpy array
data = np.array([[cell.value for cell in row] for row in ws.rows])

# Print the data
print(data)
```

## Output example

```
[[1.0, 'John', 'Smith'],
 [2.0, 'Jane', 'Doe'],
 [3.0, 'Bob', 'Jones']]
```

The code works as follows:
1. The `openpyxl` library is imported.
2. The XLSX file is opened with `openpyxl.load_workbook()`.
3. The active sheet is retrieved with `wb.active`.
4. The data from the sheet is read with a list comprehension and stored in a Numpy array with `np.array()`.
5. The data is printed with `print()`.

## Helpful links
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [Numpy](https://numpy.org/)

onelinerhub: [x

How can I use Python and Numpy to read and write data from an XLSX file?](https://onelinerhub.com/python-scipy/x--how-can-i-use-python-and-numpy-to-read-and-write-data-from-an-xlsx-file)
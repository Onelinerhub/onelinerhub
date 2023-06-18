# How do I use Python XlsxWriter to write a NumPy array to an Excel file?
// plain

Using Python XlsxWriter, you can write a NumPy array to an Excel file. Here is an example of how to do this:

```
import xlsxwriter
import numpy as np

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('arrays.xlsx')
worksheet = workbook.add_worksheet()

# Create an array of numbers
data = np.arange(1, 65).reshape(8, 8)

# Write the array to the worksheet.
worksheet.write_array('A1', data)

# Close the workbook.
workbook.close()
```

This code will create an Excel file named 'arrays.xlsx' with the NumPy array written to it.

The code consists of the following parts:
1. Importing the xlsxwriter and numpy libraries.
2. Creating a workbook and worksheet.
3. Creating an array of numbers using the numpy library.
4. Writing the array to the worksheet.
5. Closing the workbook.

## Helpful links
- [XlsxWriter documentation](https://xlsxwriter.readthedocs.io/index.html)
- [NumPy documentation](https://numpy.org/doc/)

onelinerhub: [How do I use Python XlsxWriter to write a NumPy array to an Excel file?](https://onelinerhub.com/python-scipy/how-do-i-use-python-xlsxwriter-to-write-a-numpy-array-to-an-excel-file)
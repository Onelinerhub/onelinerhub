# How do I use Python Numpy to read and write Excel (.xlsx) files?
// plain

Using Python Numpy to read and write Excel (.xlsx) files is relatively easy. To do this, you will need to import the `xlrd` and `openpyxl` modules.

## Example code

```
import xlrd
import openpyxl

# Read excel file
wb = xlrd.open_workbook('excel_file.xlsx')
sheet = wb.sheet_by_index(0)

# Write excel file
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Hello World'
wb.save('excel_file_2.xlsx')
```

The `xlrd` module is used to read the Excel (.xlsx) file, while the `openpyxl` module is used to write the Excel (.xlsx) file. The `open_workbook` method of the `xlrd` module is used to open the Excel file, while the `Workbook` method of the `openpyxl` module is used to create a new Excel file. The `sheet_by_index` method of the `xlrd` module is used to access the sheet by its index, while the `active` method of the `openpyxl` module is used to access the active sheet. Finally, the `save` method of the `openpyxl` module is used to save the Excel file.

## Code explanation

1. `import xlrd`: This imports the `xlrd` module, which is used to read the Excel (.xlsx) file.
2. `import openpyxl`: This imports the `openpyxl` module, which is used to write the Excel (.xlsx) file.
3. `wb = xlrd.open_workbook('excel_file.xlsx')`: This opens the Excel (.xlsx) file using the `open_workbook` method of the `xlrd` module.
4. `sheet = wb.sheet_by_index(0)`: This accesses the sheet by its index using the `sheet_by_index` method of the `xlrd` module.
5. `wb = openpyxl.Workbook()`: This creates a new Excel file using the `Workbook` method of the `openpyxl` module.
6. `sheet = wb.active`: This accesses the active sheet using the `active` method of the `openpyxl` module.
7. `sheet['A1'] = 'Hello World'`: This sets the value of the cell at `A1` to `Hello World`.
8. `wb.save('excel_file_2.xlsx')`: This saves the Excel file using the `save` method of the `openpyxl` module.

## Helpful links
- [xlrd Documentation](https://xlrd.readthedocs.io/en/latest/)
- [openpyxl Documentation](https://openpyxl.readthedocs.io/en/stable/)

onelinerhub: [How do I use Python Numpy to read and write Excel (.xlsx) files?](https://onelinerhub.com/python-scipy/how-do-i-use-python-numpy-to-read-and-write-excel---xlsx--files)
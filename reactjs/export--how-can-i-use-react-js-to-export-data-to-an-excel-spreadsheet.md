# export

How can I use React.js to export data to an Excel spreadsheet?
// plain

React.js can be used to export data to an Excel spreadsheet by using a library such as [js-xlsx](https://github.com/SheetJS/js-xlsx). To get started, install the library using npm:

```
npm install xlsx
```

Then, import the library into the React component:

```
import XLSX from 'xlsx';
```

To export data to an Excel spreadsheet, you'll need to first create a workbook object, and then add worksheets to the workbook object. To create the workbook object, use the `XLSX.utils.book_new()` method:

```
const workbook = XLSX.utils.book_new();
```

To add worksheets to the workbook object, use the `XLSX.utils.book_append_sheet()` method. This method takes two parameters: a worksheet object and a sheet name:

```
XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
```

To create the worksheet object, use the `XLSX.utils.aoa_to_sheet()` method. This method takes an array of arrays as a parameter. Each array in the array of arrays is a row in the worksheet. For example, the following code will create a worksheet with two rows and two columns:

```
const worksheet = XLSX.utils.aoa_to_sheet([
  ['Column 1', 'Column 2'],
  ['Value 1', 'Value 2']
]);
```

Finally, to write the workbook object to an Excel file, use the `XLSX.writeFile()` method. This method takes two parameters: the workbook object and the file name:

```
XLSX.writeFile(workbook, 'filename.xlsx');
```

This will create an Excel file named `filename.xlsx` with the data from the worksheet.

## Helpful links
* [js-xlsx](https://github.com/SheetJS/js-xlsx)
* [XLSX.utils.book_new()](https://sheetjs.gitbooks.io/docs/#xlsxutilsbook_new)
* [XLSX.utils.book_append_sheet()](https://sheetjs.gitbooks.io/docs/#xlsxutilsbook_append_sheet)
* [XLSX.utils.aoa_to_sheet()](https://sheetjs.gitbooks.io/docs/#xlsxutilsaoa_to_sheet)
* [XLSX.writeFile()](https://sheetjs.gitbooks.io/docs/#xlsxwritefile)

onelinerhub: [export

How can I use React.js to export data to an Excel spreadsheet?](https://onelinerhub.com/reactjs/export--how-can-i-use-react-js-to-export-data-to-an-excel-spreadsheet)
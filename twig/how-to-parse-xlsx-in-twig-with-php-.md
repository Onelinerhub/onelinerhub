# How to parse XLSX in Twig with PHP?
// plain

Parsing XLSX in Twig with PHP can be done using the [PHPExcel library](https://github.com/PHPOffice/PHPExcel).

```php
// Include PHPExcel library
require_once 'PHPExcel/Classes/PHPExcel.php';

// Create new PHPExcel object
$objPHPExcel = new PHPExcel();

// Load an existing XLSX file
$objPHPExcel = PHPExcel_IOFactory::load("example.xlsx");

// Get the active sheet
$objWorksheet = $objPHPExcel->getActiveSheet();

// Get the highest row and column numbers
$highestRow = $objWorksheet->getHighestRow();
$highestColumn = $objWorksheet->getHighestColumn();

// Loop through each row of the worksheet
for ($row = 1; $row <= $highestRow; $row++) {
    // Read a single row of data
    $rowData = $objWorksheet->rangeToArray('A' . $row . ':' . $highestColumn . $row, NULL, TRUE, FALSE);

    // Do something with the data
    // ...
}
```

The code above will read an existing XLSX file, `example.xlsx`, and loop through each row of the worksheet. The `$rowData` variable will contain an array of the data in the row.

- `require_once 'PHPExcel/Classes/PHPExcel.php'`: Include the PHPExcel library.
- `$objPHPExcel = new PHPExcel()`: Create a new PHPExcel object.
- `$objPHPExcel = PHPExcel_IOFactory::load("example.xlsx")`: Load an existing XLSX file.
- `$objWorksheet = $objPHPExcel->getActiveSheet()`: Get the active sheet.
- `$highestRow = $objWorksheet->getHighestRow()`: Get the highest row number.
- `$highestColumn = $objWorksheet->getHighestColumn()`: Get the highest column number.
- `$rowData = $objWorksheet->rangeToArray('A' . $row . ':' . $highestColumn . $row, NULL, TRUE, FALSE)`: Read a single row of data.

onelinerhub: [How to parse XLSX in Twig with PHP?](https://onelinerhub.com/twig/how-to-parse-xlsx-in-twig-with-php-)
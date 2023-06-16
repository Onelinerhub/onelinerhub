# How can I use PHP XLSXWriter with Laravel?
// plain

PHP XLSXWriter is a library that can be used to generate Excel files with PHP. It can be used with Laravel by installing the library with Composer.

```
composer require phpoffice/phpspreadsheet
```

Once installed, you can use the library within your Laravel application. Here is an example of how to create a simple spreadsheet with Laravel and XLSXWriter:

```
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

$spreadsheet = new Spreadsheet();
$sheet = $spreadsheet->getActiveSheet();

$sheet->setCellValue('A1', 'Hello World !');

$writer = new Xlsx($spreadsheet);
$writer->save('hello world.xlsx');
```

This example will create a spreadsheet called `hello world.xlsx` with the text `Hello World !` in cell A1.

The code consists of the following parts:

1. `use` statements - these import the classes needed from the library
2. `new Spreadsheet()` - this creates a new spreadsheet object
3. `getActiveSheet()` - this gets the active sheet from the spreadsheet
4. `setCellValue()` - this sets the value of a cell in the spreadsheet
5. `new Xlsx()` - this creates a new XLSXWriter object
6. `save()` - this saves the spreadsheet to a file

For more information, see the [PHP XLSXWriter documentation](https://github.com/PHPOffice/PhpSpreadsheet/tree/develop/samples).

onelinerhub: [How can I use PHP XLSXWriter with Laravel?](https://onelinerhub.com/php-laravel/how-can-i-use-php-xlsxwriter-with-laravel)
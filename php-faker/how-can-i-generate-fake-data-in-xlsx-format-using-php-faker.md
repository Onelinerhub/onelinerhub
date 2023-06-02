# How can I generate fake data in XLSX format using PHP Faker?
// plain

Using the PHP Faker library, you can generate fake data in XLSX format. Here is an example code block that will generate a XLSX spreadsheet with 10 rows of fake data:

```
<?php

require_once 'vendor/fzaninotto/faker/src/autoload.php';

$faker = Faker\Factory::create();

$spreadsheet = new \PhpOffice\PhpSpreadsheet\Spreadsheet();
$sheet = $spreadsheet->getActiveSheet();

for ($i = 0; $i < 10; $i++) {
    $sheet->setCellValue('A' . ($i + 1), $faker->name);
    $sheet->setCellValue('B' . ($i + 1), $faker->address);
    $sheet->setCellValue('C' . ($i + 1), $faker->phoneNumber);
    $sheet->setCellValue('D' . ($i + 1), $faker->email);
}

$writer = new \PhpOffice\PhpSpreadsheet\Writer\Xlsx($spreadsheet);
$writer->save('fake_data.xlsx');
```

This code:

1. Requires the Faker library with `require_once 'vendor/fzaninotto/faker/src/autoload.php';`
2. Creates an instance of Faker with `$faker = Faker\Factory::create();`
3. Creates a new Spreadsheet object with `$spreadsheet = new \PhpOffice\PhpSpreadsheet\Spreadsheet();`
4. Creates a new Sheet object from the Spreadsheet with `$sheet = $spreadsheet->getActiveSheet();`
5. Loops 10 times to generate fake data with `for ($i = 0; $i < 10; $i++) {...}`
6. Sets the cell values of the Sheet object with `$sheet->setCellValue('A' . ($i + 1), $faker->name);`
7. Creates a new XLSX writer object with `$writer = new \PhpOffice\PhpSpreadsheet\Writer\Xlsx($spreadsheet);`
8. Saves the Spreadsheet object to a file with `$writer->save('fake_data.xlsx');`

This will generate a XLSX spreadsheet file called `fake_data.xlsx` that contains 10 rows of fake data.

## Helpful links

- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovideren_uslocale)
- [PHP Spreadsheet Documentation](https://phpspreadsheet.readthedocs.io/en/latest/)

onelinerhub: [How can I generate fake data in XLSX format using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-data-in-xlsx-format-using-php-faker)
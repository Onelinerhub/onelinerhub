# How can I generate a PDF using PHP Faker?
// plain

Generating a PDF using PHP Faker is quite simple. The following code snippet shows how to generate a PDF containing a list of random names using PHP Faker:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$pdf = new FPDF();
$pdf->AddPage();
$pdf->SetFont('Arial','B',16);
$pdf->Cell(40,10,'Random Names');

$pdf->Ln();

foreach ($faker->words as $name) {
    $pdf->Cell(40,10,$name);
    $pdf->Ln();
}

$pdf->Output('random_names.pdf','F');
```

This code creates a PDF file named `random_names.pdf` containing a list of random names. The `require_once` statement loads the Faker library. The `Faker\Factory::create()` statement creates a Faker instance. The `FPDF` class is used to create a PDF document. The `AddPage()` method adds a new page to the document. The `SetFont()` method sets the font type, style, and size. The `Cell()` method is used to add a cell containing the list title. The `Ln()` method adds a new line. The `foreach` loop iterates through the `words` property of the Faker instance and adds each name to the document. Finally, the `Output()` method saves the document to a file.

Parts of the code:

1. `require_once 'vendor/autoload.php';` - this statement loads the Faker library.
2. `$faker = Faker\Factory::create();` - this statement creates a Faker instance.
3. `$pdf = new FPDF();` - this statement creates a PDF document.
4. `$pdf->AddPage();` - this statement adds a new page to the document.
5. `$pdf->SetFont('Arial','B',16);` - this statement sets the font type, style, and size.
6. `$pdf->Cell(40,10,'Random Names');` - this statement adds a cell containing the list title.
7. `$pdf->Ln();` - this statement adds a new line.
8. `foreach ($faker->words as $name) {` - this loop iterates through the `words` property of the Faker instance.
9. `$pdf->Cell(40,10,$name);` - this statement adds each name to the document.
10. `$pdf->Output('random_names.pdf','F');` - this statement saves the document to a file.

## Helpful links

- [FPDF Class Reference](https://www.fpdf.org/en/doc/index.php)
- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderwords)

onelinerhub: [How can I generate a PDF using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-pdf-using-php-faker)
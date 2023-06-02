# How do I create a table using PHP and TCPDF?
// plain

Creating a table using PHP and TCPDF is a relatively easy task. The following example code block will create a basic table with three columns and three rows.
```
<?php
$pdf = new TCPDF();

$pdf->AddPage();

$pdf->SetFont('helvetica', '', 11);

$pdf->Cell(40, 10, 'Column 1', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Column 2', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Column 3', 1, 1, 'C', 0, '', 0);

$pdf->Cell(40, 10, 'Row 1', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 1', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 1', 1, 1, 'C', 0, '', 0);

$pdf->Cell(40, 10, 'Row 2', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 2', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 2', 1, 1, 'C', 0, '', 0);

$pdf->Cell(40, 10, 'Row 3', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 3', 1, 0, 'C', 0, '', 0);
$pdf->Cell(40, 10, 'Row 3', 1, 1, 'C', 0, '', 0);

$pdf->Output('table.pdf', 'I');
?>
```

This code will generate a PDF file with a table that looks like this:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Row 1    | Row 1    |
| Row 2    | Row 2    | Row 2    |
| Row 3    | Row 3    | Row 3    |

The code uses the TCPDF library to create a PDF document, and the Cell() method to create the table. The parameters of this method are as follows:

* `$w`: width of the cell
* `$h`: height of the cell
* `$txt`: text to be printed inside the cell
* `$border`: specifies if borders should be drawn around the cell
* `$ln`: specifies where the current position should go after the call
* `$align`: specifies the alignment of the text inside the cell
* `$fill`: specifies if the cell background should be painted
* `$link`: link to be associated with the cell
* `$stretch`: specifies if the cell should be stretched to fit the text

For more information on how to use TCPDF to create tables, please refer to the [TCPDF documentation](https://tcpdf.org/examples/example_061/).

onelinerhub: [How do I create a table using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-create-a-table-using-php-and-tcpdf)
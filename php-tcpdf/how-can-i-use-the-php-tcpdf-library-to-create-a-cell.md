# How can I use the PHP TCPDF library to create a cell?
// plain

To use the PHP TCPDF library to create a cell, you need to include the TCPDF library in your project, then call the `Cell` method. The `Cell` method requires 3 parameters: the width, the height and the text to be displayed. Here is an example:

```php
<?php
require_once('tcpdf.php');

$pdf = new TCPDF();

$pdf->Cell(50, 10, 'Hello World!');

$pdf->Output('example.pdf', 'I');
```

This will output a PDF with a cell with a width of 50 points and a height of 10 points, containing the text "Hello World!".

The `Cell` method also has optional parameters which you can use to customize the cell. These are:

* `$border` (int): Specifies if borders should be drawn around the cell. Accepts the constants `TCPDF_CELL_BORDER_NONE`, `TCPDF_CELL_BORDER_LEFT`, `TCPDF_CELL_BORDER_TOP`, `TCPDF_CELL_BORDER_RIGHT` and `TCPDF_CELL_BORDER_BOTTOM`.
* `$ln` (int): Indicates where the current position should go after the call. Accepts the constants `0` (to the right), `1` (to the beginning of the next line), and `2` (below).
* `$align` (string): Allows to center or align the text. Accepts the constants `L` (left), `C` (center) and `R` (right).
* `$fill` (boolean): Indicates if the cell background should be painted (true) or transparent (false).
* `$link` (string): URL or identifier returned by `AddLink()`.

For more information about the `Cell` method, please refer to the [TCPDF documentation](https://tcpdf.org/doc/code/classTCPDF.html#a6c2f8d7e7e814a1f9a7e3b2b1e9b9b2c).

onelinerhub: [How can I use the PHP TCPDF library to create a cell?](https://onelinerhub.com/php-tcpdf/how-can-i-use-the-php-tcpdf-library-to-create-a-cell)
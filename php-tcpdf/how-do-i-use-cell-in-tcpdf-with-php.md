# How do I use cell in TCPDF with PHP?
// plain

Using TCPDF with PHP is quite easy. In order to use the cell function, you need to first create an instance of the TCPDF class and set the page size and orientation.

```php
$pdf = new TCPDF('P', 'mm', 'A4', true, 'UTF-8', false);
```

Then, you can use the `Cell()` function to draw a cell on the page. The `Cell()` function takes 6 parameters: the width of the cell, the height of the cell, the text that will be displayed in the cell, the border of the cell, the position of the cursor after the cell is drawn, and the alignment of the text inside the cell.

```php
$pdf->Cell(50, 10, 'Hello World!', 1, 0, 'C');
```

This will draw a cell on the page with a width of 50mm, a height of 10mm, the text "Hello World!" in the center of the cell, a border of 1, and the cursor will be moved to the right of the cell.

You can also use the `MultiCell()` function to draw a cell with multiple lines of text. This function takes 8 parameters: the width of the cell, the height of the cell, the text that will be displayed in the cell, the border of the cell, the position of the cursor after the cell is drawn, the alignment of the text inside the cell, whether or not to fill the cell with a background color, and the background color of the cell.

```php
$pdf->MultiCell(50, 10, 'Hello World!\nThis is a multi-line cell.', 1, 'C', true, 0, 0, 0, true);
```

This will draw a cell on the page with a width of 50mm, a height of 10mm, the text "Hello World!" and "This is a multi-line cell." in the center of the cell, a border of 1, the cursor will be moved to the right of the cell, the text will be centered, the cell will be filled with a background color, and the background color of the cell will be white.

For more information on the TCPDF library and its functions, please refer to the [TCPDF Documentation](https://tcpdf.org/docs/index.php).

onelinerhub: [How do I use cell in TCPDF with PHP?](https://onelinerhub.com/php-tcpdf/how-do-i-use-cell-in-tcpdf-with-php)
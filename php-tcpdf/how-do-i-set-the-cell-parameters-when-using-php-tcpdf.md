# How do I set the cell parameters when using PHP TCPDF?
// plain

You can set the cell parameters when using PHP TCPDF by using the `MultiCell()` method.

```
// set cell parameters
$pdf->MultiCell(40, 10, 'Cell 1', 1, 'C', 0, 0);
$pdf->MultiCell(40, 10, 'Cell 2', 1, 'C', 0, 0);
```

This will create two cells with a width of 40 and a height of 10. The first parameter is the width of the cell, the second is the height. The third parameter is the text to be placed in the cell. The fourth parameter is the border, the fifth is the alignment, the sixth is the fill and the seventh is the padding.

The output of the code will be two cells with the text "Cell 1" and "Cell 2" in them.

## Code explanation

- `MultiCell()`: This is the method used to set the cell parameters.
- `40, 10`: These are the width and height of the cell.
- `'Cell 1'` and `'Cell 2'`: These are the texts to be placed in the cells.
- `1`: This is the border of the cell.
- `'C'`: This is the alignment of the cell.
- `0`: This is the fill of the cell.
- `0`: This is the padding of the cell.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/source_docs/classTCPDF/#ac6f3f12ec30c10246bd681f39f451312)

onelinerhub: [How do I set the cell parameters when using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-the-cell-parameters-when-using-php-tcpdf)
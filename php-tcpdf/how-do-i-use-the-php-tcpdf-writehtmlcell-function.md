# How do I use the PHP TCPDF WriteHTMLCell function?
// plain

The `TCPDF WriteHTMLCell` function is used to write HTML content to a PDF document. It takes four parameters: the x and y coordinates of the cell, the width and height of the cell, and the HTML content to be written.

For example:

```
$pdf->WriteHTMLCell(50, 10, 10, 10, "<p>Hello World!</p>");
```

This will write the text "Hello World!" to the PDF document, starting at the x and y coordinates of 10, 10, and with a width and height of 50 and 10 respectively.

The parts of the `WriteHTMLCell` function are as follows:

1. `50`: This is the width of the cell.
2. `10`: This is the height of the cell.
3. `10`: This is the x coordinate of the cell.
4. `10`: This is the y coordinate of the cell.
5. `"<p>Hello World!</p>"`: This is the HTML content to be written.

For more information about the `WriteHTMLCell` function, see the [TCPDF documentation](https://tcpdf.org/docs/classTCPDF/#writehtmlcell).

onelinerhub: [How do I use the PHP TCPDF WriteHTMLCell function?](https://onelinerhub.com/php-tcpdf/how-do-i-use-the-php-tcpdf-writehtmlcell-function)
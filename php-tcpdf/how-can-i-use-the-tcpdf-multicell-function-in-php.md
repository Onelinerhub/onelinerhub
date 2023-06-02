# How can I use the TCPDF Multicell function in PHP?
// plain

The TCPDF Multicell function in PHP allows you to print text with line breaks to a PDF document. It is a powerful and flexible function that can be used to create complex documents.

## Example code

```
$pdf->MultiCell(50, 5, "This is a very long text\nwith multiple lines\nthat should be printed\nusing the MultiCell function", 1, 'L');
```

This code will create a multicell with a width of 50 and a height of 5. It will have a border of 1 and the text will be aligned to the left.

The list of parts in the example code are:
- `$pdf->MultiCell(50, 5, ...`: This is the function call to the MultiCell function. It specifies the width and height of the cell.
- `"This is a very long text\nwith multiple lines\nthat should be printed\nusing the MultiCell function"`: This is the text that will be printed inside the cell. It can contain line breaks.
- `1, 'L'`: This is the border and alignment of the text. The border is set to 1 and the alignment is set to left.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/code/classTCPDF.html#a4b6e17b7b5d21f7d3f3c2f8f8f9a6f7b)
- [TCPDF Examples](https://tcpdf.org/examples/)

onelinerhub: [How can I use the TCPDF Multicell function in PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-use-the-tcpdf-multicell-function-in-php)
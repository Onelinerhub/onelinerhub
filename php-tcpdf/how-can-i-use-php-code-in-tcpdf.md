# How can I use PHP code in TCPDF?
// plain

PHP code can be used in TCPDF by using the `writeHTML()` method. This method allows you to pass HTML and CSS code as a string, which will be parsed and rendered into the PDF document.

## Example code

```
<?php
$html = '<h1>Hello World</h1>';
$pdf->writeHTML($html);
?>
```

This example code will render the string `<h1>Hello World</h1>` as an `h1` heading in the PDF document.

To use additional styling, you can pass a string containing CSS code to the `writeHTML()` method.

## Example code

```
<?php
$html = '<h1 style="color: red;">Hello World</h1>';
$pdf->writeHTML($html);
?>
```

This example code will render the string `<h1>Hello World</h1>` as an `h1` heading in red.

The `writeHTML()` method also accepts an array of HTML tags, which can be used to render multiple elements in the PDF document.

## Example code

```
<?php
$html = array('<h1>Hello World</h1>', '<p>This is a paragraph</p>');
$pdf->writeHTML($html);
?>
```

This example code will render the `h1` heading and the `p` paragraph in the PDF document.

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/source_docs/classTCPDF/#a0e8b3b2bfe6b7e6c5e9d7d1d0a7c9a2)
- [TCPDF Example](https://tcpdf.org/examples/example_001/)

onelinerhub: [How can I use PHP code in TCPDF?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-code-in-tcpdf)
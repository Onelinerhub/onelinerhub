# How do I set the page orientation when using PHP TCPDF?
// plain

To set the page orientation when using PHP TCPDF, use the `setPageOrientation()` method. This method takes two parameters: the page orientation (`P` for portrait or `L` for landscape) and the page format (e.g. `A4`).

For example:

```
$pdf->setPageOrientation('L', 'A4');
```

This will set the page orientation to landscape and the page format to A4.

The parts of this code are:
- `$pdf`: the TCPDF object
- `setPageOrientation()`: the method used to set the page orientation
- `'L'`: the page orientation (`P` for portrait or `L` for landscape)
- `'A4'`: the page format

For more information, see the [TCPDF documentation on setPageOrientation()](https://tcpdf.org/docs/source_docs/classTCPDF/#a4b0f7b1f3b9c2e8d7d5e1b9e9a3a6b8).

onelinerhub: [How do I set the page orientation when using PHP TCPDF?](https://onelinerhub.com/php-tcpdf/how-do-i-set-the-page-orientation-when-using-php-tcpdf)
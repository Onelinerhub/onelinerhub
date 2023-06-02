# break

How can I add a line break in a PHP document using TCPDF?
// plain

You can add a line break in a PHP document using TCPDF by using the MultiCell() method. This method allows you to create a cell with a line break. Here is an example code block:
```
$pdf->MultiCell(40,5,'This is a line
break example',1,'L');
```

The parts of the code are as follows:

* 40 - The width of the cell
* 5 - The height of the cell
* 'This is a line break example' - The text to be included in the cell
* 1 - The border of the cell, 1 is for a solid border
* 'L' - The alignment of the text within the cell, 'L' is for left aligned

The output of the code above will be a cell with the text "This is a line break example" and a line break between the two words.

For more information on the MultiCell() method, please refer to the [TCPDF documentation](https://tcpdf.org/doc/code/classTCPDF.html#a6f2c9d17f8b3f9ccf9a9c2e0f890f3f2).

onelinerhub: [break

How can I add a line break in a PHP document using TCPDF?](https://onelinerhub.com/php-tcpdf/break--how-can-i-add-a-line-break-in-a-php-document-using-tcpdf)
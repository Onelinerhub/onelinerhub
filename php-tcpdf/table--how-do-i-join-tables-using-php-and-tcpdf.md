# table

How do I join tables using PHP and TCPDF?
// plain

Joining tables in PHP and TCPDF can be done using the `TCPDF::MultiCell` method. This method allows you to join two or more tables together in a single cell. The code sample below shows how to join two tables together and display the result in a single cell:

```
$pdf->MultiCell(100, 10,
    '<table><tr><td>Table 1</td><td>Table 2</td></tr></table>',
    1, 'L', 0, 0, '', '', true, 0, false, true, 0);
```

The code above will output:

```
Table 1 Table 2
```

The code consists of the following parts:

- `$pdf->MultiCell`: This is the method call which is used to join tables together.
- `100, 10`: This is the width and height of the cell.
- `<table><tr><td>Table 1</td><td>Table 2</td></tr></table>`: This is the HTML code for the two tables which will be joined together.
- `1, 'L', 0, 0, '', '', true, 0, false, true, 0`: These are the parameters which are used to control the formatting of the cell.

For more information, please refer to the following links:

- [TCPDF::MultiCell](https://tcpdf.org/doc/class-TCPDF/#a_MultiCell)
- [TCPDF MultiCell Parameters](https://tcpdf.org/doc/code/classTCPDF.html#acdcb8f3b9f3d9545170858fb8a5a9a8c)

onelinerhub: [table

How do I join tables using PHP and TCPDF?](https://onelinerhub.com/php-tcpdf/table--how-do-i-join-tables-using-php-and-tcpdf)
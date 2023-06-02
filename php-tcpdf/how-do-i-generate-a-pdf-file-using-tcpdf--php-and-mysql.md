# How do I generate a PDF file using TCPDF, PHP and MySQL?
// plain

Using TCPDF, PHP and MySQL, you can generate a PDF file with the following steps:

1. Include the TCPDF library in your project:
```
require_once('tcpdf_include.php');
```

2. Create a new PDF document:
```
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

3. Connect to the MySQL database:
```
$db = new mysqli('host', 'username', 'password', 'database');
```

4. Retrieve data from the database:
```
$sql = "SELECT * FROM table";
$result = $db->query($sql);
```

5. Iterate through the result and add content to the PDF:
```
while ($row = $result->fetch_assoc()) {
  $pdf->Cell(0, 0, $row['field_name'], 0, 1);
}
```

6. Output the PDF to the browser:
```
$pdf->Output('example.pdf', 'I');
```

7. Close the database connection:
```
$db->close();
```

## Helpful links
- [TCPDF Documentation](https://tcpdf.org/docs/index.php)
- [PHP MySQLi Tutorial](https://www.w3schools.com/php/php_mysql_intro.asp)

onelinerhub: [How do I generate a PDF file using TCPDF, PHP and MySQL?](https://onelinerhub.com/php-tcpdf/how-do-i-generate-a-pdf-file-using-tcpdf--php-and-mysql)
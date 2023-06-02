# How can I generate a PDF from data stored in a MySQL database using TCPDF and PHP?
// plain

The following steps can be used to generate a PDF from data stored in a MySQL database using TCPDF and PHP:

1. Include the TCPDF library in your PHP code:
```php
require_once('tcpdf_include.php');
```

2. Connect to the MySQL database:
```php
$host = "localhost";
$username = "username";
$password = "password";
$dbname = "databasename";

$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
```

3. Create a query to retrieve the data you need for the PDF:
```php
$sql = "SELECT * FROM users";
$result = $conn->query($sql);
```

4. Create a new PDF document using the TCPDF library:
```php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

5. Add content to the PDF document:
```php
// set document information
$pdf->SetCreator(PDF_CREATOR);
$pdf->SetAuthor('John Doe');
$pdf->SetTitle('Users Report');
$pdf->SetSubject('TCPDF Tutorial');
$pdf->SetKeywords('TCPDF, PDF, example, test, guide');

// add a page
$pdf->AddPage();

// create some HTML content
$html = '<h1>Users Report</h1>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>';

// output data from database
while($row = $result->fetch_assoc()) {
    $html .= '<tr>
                <td>'.$row['id'].'</td>
                <td>'.$row['name'].'</td>
                <td>'.$row['email'].'</td>
            </tr>';
}

$html .= '</table>';

// output the HTML content
$pdf->writeHTML($html, true, false, true, false, '');
```

6. Output the PDF document:
```php
$pdf->Output('example_001.pdf', 'I');
```

7. Close the MySQL connection:
```php
$conn->close();
```

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs.php)
- [PHP MySQLi Connect Tutorial](https://www.w3schools.com/php/php_mysql_connect.asp)

onelinerhub: [How can I generate a PDF from data stored in a MySQL database using TCPDF and PHP?](https://onelinerhub.com/php-tcpdf/how-can-i-generate-a-pdf-from-data-stored-in-a-mysql-database-using-tcpdf-and-php)
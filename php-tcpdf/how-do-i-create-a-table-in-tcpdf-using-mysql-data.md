# How do I create a table in TCPDF using MySQL data?
// plain

In order to create a table in TCPDF using MySQL data, you need to:

1. Connect to the MySQL database and execute a query to get the data you need.

```
<?php
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, firstname, lastname FROM MyGuests";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
```

## Output example

```
id: 1 - Name: John Doe
id: 2 - Name: Mary Moe
id: 3 - Name: July Dooley
```

2. Create a new TCPDF object and set the page size and orientation.

```
<?php
$pdf = new TCPDF(PDF_PAGE_ORIENTATION, PDF_UNIT, PDF_PAGE_FORMAT, true, 'UTF-8', false);
```

3. Add a page to the PDF.

```
<?php
$pdf->AddPage();
```

4. Set the font and font size.

```
<?php
$pdf->SetFont('helvetica', '', 8);
```

5. Create the table using the data in your MySQL query.

```
<?php
$tbl = '<table cellspacing="0" cellpadding="1" border="1">';
$tbl .= '<tr><td>ID</td><td>First Name</td><td>Last Name</td></tr>';

while($row = $result->fetch_assoc()) {
    $tbl .= '<tr><td>'.$row['id'].'</td><td>'.$row['firstname'].'</td><td>'.$row['lastname'].'</td></tr>';
}

$tbl .= '</table>';
```

6. Write the table data to the PDF.

```
<?php
$pdf->writeHTML($tbl, true, false, false, false, '');
```

7. Output the PDF.

```
<?php
$pdf->Output('example_001.pdf', 'I');
```

## Helpful links

- [TCPDF Documentation](https://tcpdf.org/docs/index.php)
- [MySQL Documentation](https://dev.mysql.com/doc/)

onelinerhub: [How do I create a table in TCPDF using MySQL data?](https://onelinerhub.com/php-tcpdf/how-do-i-create-a-table-in-tcpdf-using-mysql-data)
# How to export data from MySQL to Excel using PHP?
// plain

Exporting data from MySQL to Excel using PHP is a simple process. The following example code will export the data from a MySQL table to an Excel file:
```
<?php
$connect = mysqli_connect("localhost", "username", "password", "database_name");
$output = '';
$sql = "SELECT * FROM table_name";
$result = mysqli_query($connect, $sql);
if(mysqli_num_rows($result) > 0)
{
 $output .= '
  <table class="table" bordered="1">
   <tr>
    <th>Name</th>
    <th>Address</th>
    <th>City</th>
   </tr>
 ';
 while($row = mysqli_fetch_array($result))
 {
  $output .= '
   <tr>
    <td>'.$row["name"].'</td>
    <td>'.$row["address"].'</td>
    <td>'.$row["city"].'</td>
   </tr>
  ';
 }
 $output .= '</table>';
 header('Content-Type: application/xls');
 header('Content-Disposition: attachment; filename=download.xls');
 echo $output;
}
?>
```
This code will output an Excel file with the data from the MySQL table.

The code consists of the following parts:
1. Connecting to the MySQL database using `mysqli_connect()`
2. Creating an SQL query to select the data from the table using `$sql`
3. Executing the query using `mysqli_query()`
4. Looping through the results using `mysqli_fetch_array()`
5. Creating an HTML table with the data using `$output`
6. Setting the headers for the Excel file using `header()`
7. Outputting the Excel file using `echo`

## Helpful links
- [PHP MySQLi](https://www.php.net/manual/en/book.mysqli.php)
- [PHP header()](https://www.php.net/manual/en/function.header.php)

onelinerhub: [How to export data from MySQL to Excel using PHP?](https://onelinerhub.com/php-mysql/how-to-export-data-from-mysql-to-excel-using-php)
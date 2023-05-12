# How to insert a date into a MySQL database using PHP?
// plain

To insert a date into a MySQL database using PHP, you can use the `mysqli_query()` function. The following example code will insert a date into the `date_column` of the `table_name` table:

```
$date = date("Y-m-d");
$sql = "INSERT INTO table_name (date_column) VALUES ('$date')";
if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
```

## Output example

```
New record created successfully
```

## Code explanation

- `$date = date("Y-m-d");`: This line creates a date string in the format of `YYYY-MM-DD` and stores it in the `$date` variable.
- `$sql = "INSERT INTO table_name (date_column) VALUES ('$date')";`: This line creates an SQL query to insert the date stored in the `$date` variable into the `date_column` of the `table_name` table.
- `if (mysqli_query($conn, $sql)) {`: This line checks if the query was successful.
- `echo "New record created successfully";`: This line prints a success message if the query was successful.
- `echo "Error: " . $sql . "<br>" . mysqli_error($conn);`: This line prints an error message if the query was unsuccessful.

## Helpful links
- [PHP date() Function](https://www.w3schools.com/php/func_date_date.asp)
- [MySQL INSERT INTO Statement](https://www.w3schools.com/sql/sql_insert.asp)
- [MySQLi query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)

onelinerhub: [How to insert a date into a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-insert-a-date-into-a-mysql-database-using-php)
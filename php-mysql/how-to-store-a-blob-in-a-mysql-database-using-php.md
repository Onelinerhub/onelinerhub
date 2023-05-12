# How to store a BLOB in a MySQL database using PHP?
// plain

Storing a BLOB (Binary Large Object) in a MySQL database using PHP can be done by using the `mysqli_query()` function. The following example code will store a BLOB in the `files` table of the `mydb` database:

```
$conn = mysqli_connect("localhost", "my_user", "my_password", "mydb");
$sql = "INSERT INTO files (name, type, size, content ) ".
"VALUES ('$fileName', '$fileType', '$fileSize', '$content')";
$result = mysqli_query($conn, $sql);
```

The output of the above code will be a `TRUE` or `FALSE` value, depending on whether the query was successful or not.

## Code explanation


1. `mysqli_connect()`: Establishes a connection to the MySQL database.
2. `$sql`: The SQL query used to insert the BLOB into the database.
3. `$result`: Stores the result of the query.
4. `mysqli_query()`: Executes the SQL query.

## Helpful links

- [MySQL: Inserting BLOBs with PHP](https://dev.mysql.com/doc/refman/8.0/en/blob.html)
- [PHP: mysqli_query()](https://www.php.net/manual/en/mysqli.query.php)

onelinerhub: [How to store a BLOB in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-store-a-blob-in-a-mysql-database-using-php)
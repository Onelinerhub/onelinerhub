# How to update to null value in MySQL using PHP?
// plain

Updating a null value in MySQL using PHP can be done using the `UPDATE` statement. The following example code will update the `name` column of the `users` table to `NULL` if the `id` is `1`:

```
$sql = "UPDATE users SET name = NULL WHERE id = 1";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}
```

## Output example

```
Record updated successfully
```

## Code explanation

- `$sql`: This is the SQL statement that will be used to update the `name` column of the `users` table to `NULL` if the `id` is `1`.
- `$conn->query($sql)`: This is the function that will execute the SQL statement.
- `echo "Record updated successfully"`: This is the output that will be displayed if the record is updated successfully.
- `echo "Error updating record: " . $conn->error`: This is the output that will be displayed if there is an error updating the record.

## Helpful links
- [MySQL UPDATE Statement](https://www.w3schools.com/sql/sql_update.asp)
- [MySQL PHP Reference](https://www.php.net/manual/en/ref.mysql.php)

onelinerhub: [How to update to null value in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-update-to-null-value-in-mysql-using-php)
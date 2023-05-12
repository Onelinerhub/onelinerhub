# How to get a key-value array from a MySQL database using PHP?
// plain

Using PHP, you can get a key-value array from a MySQL database by executing a query and looping through the results.

```
$query = "SELECT * FROM table";
$result = mysqli_query($conn, $query);
$array = array();
while ($row = mysqli_fetch_assoc($result)) {
    $array[$row['key']] = $row['value'];
}
```

The output of the above code will be an associative array with the keys and values from the database.

## Code explanation


1. `$query = "SELECT * FROM table";` - This line creates a query to select all columns from the table.

2. `$result = mysqli_query($conn, $query);` - This line executes the query and stores the result in the `$result` variable.

3. `$array = array();` - This line creates an empty array to store the key-value pairs.

4. `while ($row = mysqli_fetch_assoc($result)) {` - This line starts a loop to iterate through the results of the query.

5. `$array[$row['key']] = $row['value'];` - This line adds the key-value pair from the current row to the array.

## Helpful links

- [MySQL SELECT Query](https://www.w3schools.com/sql/sql_select.asp)
- [PHP mysqli_query() Function](https://www.w3schools.com/php/func_mysqli_query.asp)
- [PHP mysqli_fetch_assoc() Function](https://www.w3schools.com/php/func_mysqli_fetch_assoc.asp)

onelinerhub: [How to get a key-value array from a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-get-a-key-value-array-from-a-mysql-database-using-php)
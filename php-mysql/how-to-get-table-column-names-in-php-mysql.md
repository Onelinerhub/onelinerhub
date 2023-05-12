# How to get table column names in PHP MySQL?
// plain

To get the column names of a table in PHP MySQL, you can use the `mysqli_fetch_fields()` function. This function returns an array of objects containing the column names.

## Example code

```
$conn = mysqli_connect("localhost", "username", "password", "database");
$sql = "SELECT * FROM table";
$result = mysqli_query($conn, $sql);
$columns = mysqli_fetch_fields($result);

foreach ($columns as $column) {
    echo $column->name . "\n";
}
```

## Output example

```
column1
column2
column3
```

## Code explanation

- `mysqli_fetch_fields($result)`: This function takes the result of a query as an argument and returns an array of objects containing the column names.
- `$column->name`: This is used to access the name of each column in the array of objects returned by `mysqli_fetch_fields()`.

## Helpful links
- [PHP mysqli_fetch_fields() Function](https://www.w3schools.com/php/func_mysqli_fetch_fields.asp)

onelinerhub: [How to get table column names in PHP MySQL?](https://onelinerhub.com/php-mysql/how-to-get-table-column-names-in-php-mysql)
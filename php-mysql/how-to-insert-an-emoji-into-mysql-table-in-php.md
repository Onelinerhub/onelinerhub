# How to insert an emoji into MySQL table in PHP?
// plain

To insert an emoji into a MySQL table in PHP, you can use the `mysqli_real_escape_string()` function. This function takes a string as an argument and returns a string with special characters escaped.

## Example code

```php
$emoji = "😃";
$escaped_emoji = mysqli_real_escape_string($conn, $emoji);
$sql = "INSERT INTO table_name (emoji_column) VALUES ('$escaped_emoji')";
```

The code above will insert the emoji into the `table_name` table in the `emoji_column` column.

## Code explanation

- `$emoji`: a variable containing the emoji to be inserted
- `mysqli_real_escape_string($conn, $emoji)`: a function that takes a connection and a string as arguments and returns a string with special characters escaped
- `$sql`: a variable containing the SQL query to insert the emoji into the table

## Helpful links
- [PHP mysqli_real_escape_string() Function](https://www.w3schools.com/php/func_mysqli_real_escape_string.asp)
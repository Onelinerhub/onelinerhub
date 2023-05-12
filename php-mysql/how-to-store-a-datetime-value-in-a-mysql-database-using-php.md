# How to store a datetime value in a MySQL database using PHP?
// plain

Storing a datetime value in a MySQL database using PHP is a simple process. The following example code block can be used to store a datetime value in a MySQL database:
```
$date = date('Y-m-d H:i:s');
$sql = "INSERT INTO table_name (date_column) VALUES ('$date')";
```
The code above will insert the current date and time into the `date_column` of the `table_name` table.

The code consists of two parts:
1. `$date = date('Y-m-d H:i:s');` - This line of code uses the `date()` function to get the current date and time in the `Y-m-d H:i:s` format.
2. `$sql = "INSERT INTO table_name (date_column) VALUES ('$date')";` - This line of code creates an SQL query to insert the `$date` value into the `date_column` of the `table_name` table.

For more information, please refer to the following links:
- [PHP date() Function](https://www.w3schools.com/php/func_date_date.asp)
- [MySQL INSERT INTO Statement](https://www.w3schools.com/sql/sql_insert.asp)

onelinerhub: [How to store a datetime value in a MySQL database using PHP?](https://onelinerhub.com/php-mysql/how-to-store-a-datetime-value-in-a-mysql-database-using-php)
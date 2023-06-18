# How can I use PHP to query a SQLite database?
// plain

Using PHP to query a SQLite database is relatively easy. The following example code block will illustrate how to do this:
```
<?php
// Connect to the database
$db = new SQLite3('mydatabase.sqlite');
// Create a query
$query = "SELECT * FROM mytable";
// Execute the query
$result = $db->query($query);
// Loop through the results
while ($row = $result->fetchArray()) {
    echo "Name: " . $row['name'] . "<br />";
    echo "Age: " . $row['age'] . "<br />";
}
?>
```
This code will output something like this:
```
Name: John Doe
Age: 33
Name: Jane Doe
Age: 28
```

This code consists of the following parts:
1. `$db = new SQLite3('mydatabase.sqlite');` - This part creates a connection to the SQLite database.
2. `$query = "SELECT * FROM mytable";` - This part creates a query that will select all data from the table `mytable`.
3. `$result = $db->query($query);` - This part executes the query.
4. `while ($row = $result->fetchArray()) {...}` - This part loops through the results of the query.
5. `echo "Name: " . $row['name'] . "<br />";` - This part prints out the name from the result.

For more information and examples on how to use PHP to query a SQLite database, please see the following links:
* [PHP SQLite3](https://www.php.net/manual/en/book.sqlite3.php)
* [SQLite3::query](https://www.php.net/manual/en/sqlite3.query.php)
* [SQLite3::fetchArray](https://www.php.net/manual/en/sqlite3.fetcharray.php)

onelinerhub: [How can I use PHP to query a SQLite database?](https://onelinerhub.com/sqlite/how-can-i-use-php-to-query-a-sqlite-database)
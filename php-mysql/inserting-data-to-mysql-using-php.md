# Inserting data to MySQL using PHP
// plain

Inserting data to MySQL using PHP is a common task for web developers. It can be done using the `mysqli_query()` function. The following example code inserts a new record into a table called `users`:

```
$sql = "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')";
mysqli_query($conn, $sql);
```

The code above will insert a new record with the name `John Doe` and email `john@example.com` into the `users` table.

The code consists of two parts:

1. The SQL query: `$sql = "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')";`
   - This part of the code defines the SQL query that will be used to insert the data.
2. The `mysqli_query()` function: `mysqli_query($conn, $sql);`
   - This part of the code executes the SQL query and inserts the data into the database.

## Helpful links

- [PHP MySQL Insert](https://www.w3schools.com/php/php_mysql_insert.asp)
- [MySQL INSERT Statement](https://www.w3schools.com/sql/sql_insert.asp)

onelinerhub: [Inserting data to MySQL using PHP](https://onelinerhub.com/php-mysql/inserting-data-to-mysql-using-php)
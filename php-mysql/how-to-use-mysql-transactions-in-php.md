# How to use MySQL transactions in PHP?
// plain

MySQL transactions are used to ensure data integrity and atomicity when performing multiple operations on a database. Transactions are started with the `begin` statement and committed with the `commit` statement.

## Example code

```
<?php
$conn = new mysqli("localhost", "user", "password", "database");

// Start transaction
$conn->begin_transaction();

// Perform queries
$conn->query("INSERT INTO table (column1, column2) VALUES (value1, value2)");
$conn->query("UPDATE table SET column1 = value1 WHERE column2 = value2");

// Commit transaction
$conn->commit();

$conn->close();
?>
```

## Output example

```
No output
```

## Code explanation


1. `$conn = new mysqli("localhost", "user", "password", "database");` - Establishes a connection to the MySQL database.
2. `$conn->begin_transaction();` - Starts a transaction.
3. `$conn->query("INSERT INTO table (column1, column2) VALUES (value1, value2)");` - Inserts a row into the table.
4. `$conn->query("UPDATE table SET column1 = value1 WHERE column2 = value2");` - Updates a row in the table.
5. `$conn->commit();` - Commits the transaction.
6. `$conn->close();` - Closes the connection to the MySQL database.

## Helpful links

1. [MySQL Transactions](https://dev.mysql.com/doc/refman/8.0/en/commit.html)
2. [PHP MySQL Transactions](https://www.w3schools.com/php/php_mysql_transactions.asp)

onelinerhub: [How to use MySQL transactions in PHP?](https://onelinerhub.com/php-mysql/how-to-use-mysql-transactions-in-php)
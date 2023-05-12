# How to begin MySQL transaction in PHP?
// plain

MySQL transactions can be started in PHP using the `mysqli_begin_transaction()` function. This function takes a single parameter, which is a `mysqli` object.

```php
$mysqli = new mysqli("localhost", "user", "password", "database");

if (mysqli_begin_transaction($mysqli)) {
    // Transaction started successfully
} else {
    // Transaction failed to start
}
```

The code above creates a new `mysqli` object and then attempts to start a transaction using the `mysqli_begin_transaction()` function. If the transaction is started successfully, the code inside the `if` block will be executed. Otherwise, the code inside the `else` block will be executed.

## Code explanation


- `mysqli_begin_transaction()`: This function is used to start a MySQL transaction.
- `$mysqli`: This is a `mysqli` object that is used to connect to the MySQL database.
- `if`: This is a control structure that is used to execute code based on a condition.
- `else`: This is a control structure that is used to execute code if the condition in the `if` statement is not met.

## Helpful links

- [MySQL: Transactions](https://dev.mysql.com/doc/refman/8.0/en/commit.html)
- [PHP: mysqli_begin_transaction](https://www.php.net/manual/en/mysqli.begin-transaction.php)

onelinerhub: [How to begin MySQL transaction in PHP?](https://onelinerhub.com/php-mysql/how-to-begin-mysql-transaction-in-php)
# How to use multiple prepared statements in PHP and MySQL?
// plain

Using multiple prepared statements in PHP and MySQL is a great way to ensure that your code is secure and efficient. Prepared statements allow you to write code that is more secure and efficient than using regular SQL queries.

## Example code

```
$stmt1 = $db->prepare("SELECT * FROM users WHERE id = ?");
$stmt1->bind_param("i", $user_id);
$stmt1->execute();

$stmt2 = $db->prepare("SELECT * FROM posts WHERE user_id = ?");
$stmt2->bind_param("i", $user_id);
$stmt2->execute();
```

## Output example

```
No output
```

## Code explanation


1. `$stmt1 = $db->prepare("SELECT * FROM users WHERE id = ?");` - This line prepares a statement to select all columns from the users table where the id is equal to the value of the `$user_id` variable.

2. `$stmt1->bind_param("i", $user_id);` - This line binds the `$user_id` variable to the prepared statement.

3. `$stmt1->execute();` - This line executes the prepared statement.

4. `$stmt2 = $db->prepare("SELECT * FROM posts WHERE user_id = ?");` - This line prepares a statement to select all columns from the posts table where the user_id is equal to the value of the `$user_id` variable.

5. `$stmt2->bind_param("i", $user_id);` - This line binds the `$user_id` variable to the prepared statement.

6. `$stmt2->execute();` - This line executes the prepared statement.

## Helpful links

- [PHP MySQL Prepared Statements](https://www.w3schools.com/php/php_mysql_prepared_statements.asp)
- [MySQL Prepared Statements](https://dev.mysql.com/doc/refman/8.0/en/sql-syntax-prepared-statements.html)

onelinerhub: [How to use multiple prepared statements in PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-use-multiple-prepared-statements-in-php-and-mysql)
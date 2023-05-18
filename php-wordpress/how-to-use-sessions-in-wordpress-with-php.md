# How to use sessions in WordPress with PHP?
// plain

Sessions in WordPress with PHP can be used to store data across multiple pages. This is done by using the `session_start()` function.

```php
<?php
session_start();
$_SESSION['name'] = 'John Doe';
?>
```

The code above will start a session and store the name `John Doe` in the `$_SESSION` array.

## Code explanation


1. `session_start()` - This function starts a new session or resumes an existing one.
2. `$_SESSION['name']` - This is an associative array that stores data in the session.
3. `'John Doe'` - This is the data that is stored in the `$_SESSION` array.

## Helpful links

- [PHP Sessions](https://www.php.net/manual/en/book.session.php)
- [WordPress Sessions](https://codex.wordpress.org/Session_Management)

onelinerhub: [How to use sessions in WordPress with PHP?](https://onelinerhub.com/php-wordpress/how-to-use-sessions-in-wordpress-with-php)
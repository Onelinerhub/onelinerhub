# How to check if a user is logged in in WordPress using PHP?
// plain

To check if a user is logged in in WordPress using PHP, you can use the `is_user_logged_in()` function. This function returns a boolean value, `true` if the user is logged in, and `false` if the user is not logged in.

## Example code

```
if ( is_user_logged_in() ) {
    // user is logged in
} else {
    // user is not logged in
}
```

## Output example

```
// no output
```

## Code explanation

- `is_user_logged_in()`: This is the function used to check if a user is logged in.
- `if` statement: This is used to check the boolean value returned by the `is_user_logged_in()` function.
- `true`: This is the value returned by the `is_user_logged_in()` function if the user is logged in.
- `false`: This is the value returned by the `is_user_logged_in()` function if the user is not logged in.

## Helpful links
- [WordPress Codex - is_user_logged_in()](https://codex.wordpress.org/Function_Reference/is_user_logged_in)

onelinerhub: [How to check if a user is logged in in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-check-if-a-user-is-logged-in-in-wordpress-using-php)
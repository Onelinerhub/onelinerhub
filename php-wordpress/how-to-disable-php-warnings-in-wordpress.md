# How to disable PHP warnings in WordPress?
// plain

To disable PHP warnings in WordPress, you can add the following code to your `wp-config.php` file:
```
error_reporting(0);
@ini_set('display_errors', 0);
```
This will suppress all PHP warnings and errors from being displayed on the WordPress site.

## Code explanation

- `error_reporting(0);` - This line sets the error reporting level to 0, which will suppress all warnings and errors.
- `@ini_set('display_errors', 0);` - This line sets the display_errors setting to 0, which will prevent any errors from being displayed on the WordPress site.

## Helpful links
- [WordPress Codex - Debugging in WordPress](https://codex.wordpress.org/Debugging_in_WordPress)
- [PHP Manual - error_reporting](http://php.net/manual/en/function.error-reporting.php)
- [PHP Manual - ini_set](http://php.net/manual/en/function.ini-set.php)

onelinerhub: [How to disable PHP warnings in WordPress?](https://onelinerhub.com/php-wordpress/how-to-disable-php-warnings-in-wordpress)
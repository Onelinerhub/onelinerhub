# How to redirect to another page in WordPress using PHP?
// plain

Redirecting to another page in WordPress using PHP is a simple process. The following example code block will redirect the user to a page with the URL `http://example.com/new-page`:
```
wp_redirect( 'http://example.com/new-page' );
exit;
```
The code consists of two parts:
1. `wp_redirect()`: This function redirects the user to the specified URL.
2. `exit;`: This statement terminates the script execution.

For more information, please refer to the [WordPress Codex](https://codex.wordpress.org/Function_Reference/wp_redirect).

onelinerhub: [How to redirect to another page in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-redirect-to-another-page-in-wordpress-using-php)
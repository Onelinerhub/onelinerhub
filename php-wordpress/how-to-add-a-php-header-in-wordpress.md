# How to add a PHP header in WordPress?
// plain

Adding a PHP header in WordPress is a simple process. To do this, you need to use the `header()` function. This function takes two parameters: the header name and the header value.

```
<?php
header("Content-Type: text/html; charset=utf-8");
?>
```

This code will add a header with the name `Content-Type` and the value `text/html; charset=utf-8`.

## Code explanation


1. `<?php` - This is the opening PHP tag.
2. `header()` - This is the function used to add a header.
3. `"Content-Type"` - This is the header name.
4. `"text/html; charset=utf-8"` - This is the header value.
5. `?>` - This is the closing PHP tag.

## Helpful links

- [PHP header() Function](https://www.w3schools.com/php/func_network_header.asp)
- [WordPress Codex: Using PHP in WordPress](https://codex.wordpress.org/Using_PHP_in_WordPress)

onelinerhub: [How to add a PHP header in WordPress?](https://onelinerhub.com/php-wordpress/how-to-add-a-php-header-in-wordpress)
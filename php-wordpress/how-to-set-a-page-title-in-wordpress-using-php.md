# How to set a page title in WordPress using PHP?
// plain

Setting a page title in WordPress using PHP is a simple process. The following example code block will set the page title to "My Page Title":
```
<?php
  $title = "My Page Title";
  wp_title($title);
?>
```
This code will output the page title as "My Page Title".

The code consists of two parts:
1. The first part is the variable declaration, which sets the value of the variable `$title` to "My Page Title".
2. The second part is the `wp_title()` function, which takes the value of the `$title` variable and sets it as the page title.

For more information on setting page titles in WordPress using PHP, please refer to the following links:
- [WordPress Codex - wp_title()](https://codex.wordpress.org/Function_Reference/wp_title)
- [WordPress Codex - The Loop](https://codex.wordpress.org/The_Loop)

onelinerhub: [How to set a page title in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-set-a-page-title-in-wordpress-using-php)
# Remove Login Form Errors From Wordpress Login Form

```php
add_filter('login_errors',create_function('$a', "return null;"));

```

add this code in function.php current active theme
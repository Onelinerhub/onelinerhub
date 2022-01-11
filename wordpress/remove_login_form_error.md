# Remove errors from Wordpress login form

```php
add_filter('login_errors', create_function('$a', "return null;"));
```

- `add_filter` - registers new filter
- `login_errors` - attach filter to login_errors
- `return null` - do nothing



# Disable post revisions from Wordpress

### Add this to `wp-config.php` file:

```php
define('WP_POST_REVISIONS', false);
```

- `define` - defines PHP constant
- `WP_POST_REVISIONS` - enabled post revisions (set to `false` to disable)



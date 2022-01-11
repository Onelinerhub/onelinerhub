# Fix SVG file Upload Problem in Wordpress

```php
add_filter('upload_mimes', 'my_upload_mimes');
function my_upload_mimes($mimes = array()) {
    $mimes['svg'] = 'image/svg+xml';
    return $mimes;
}
```

add this code in function.php current active theme
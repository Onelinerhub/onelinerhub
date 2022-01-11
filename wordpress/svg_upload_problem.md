# Fix SVG file upload problem in Wordpress

```php
add_filter('upload_mimes', 'my_upload_mimes');

function my_upload_mimes($mimes = array()) {
    $mimes['svg'] = 'image/svg+xml';
    return $mimes;
}
```

- `add_filter` - registers new filter
- `upload_mimes` - attach to "upload_mimes" filter
- `my_upload_mimes` - custom function handler to add new supported mime
- `$mimes['svg'] = 'image/svg+xml';` - register new mime for SVG



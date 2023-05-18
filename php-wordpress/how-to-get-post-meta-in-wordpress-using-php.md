# How to get post meta in WordPress using PHP?
// plain

Getting post meta in WordPress using PHP is a simple process. You can use the `get_post_meta()` function to retrieve post meta data.

```php
$post_meta = get_post_meta( $post_id, $key, $single );
```

The `get_post_meta()` function takes three parameters:

- `$post_id`: The ID of the post to retrieve meta data from.
- `$key`: The meta key to retrieve.
- `$single`: Whether to return a single value or an array.

The output of the `get_post_meta()` function is an array of post meta data.

```
Array
(
    [0] => post_meta_value
)
```

For more information, see the [WordPress Codex](https://codex.wordpress.org/Function_Reference/get_post_meta).

onelinerhub: [How to get post meta in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-get-post-meta-in-wordpress-using-php)
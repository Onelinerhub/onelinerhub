# How to use the WordPress REST API with PHP?
// plain

The WordPress REST API is a powerful tool for interacting with WordPress sites remotely. It can be used with PHP to create custom applications that interact with WordPress data.

To use the WordPress REST API with PHP, you need to make an HTTP request to the API endpoint. For example, to get a list of posts from a WordPress site, you can use the following code:

```php
$response = wp_remote_get( 'https://example.com/wp-json/wp/v2/posts' );
$posts = json_decode( wp_remote_retrieve_body( $response ) );
```

The code above will make an HTTP request to the `wp-json/wp/v2/posts` endpoint and store the response in the `$response` variable. The response is then decoded into a PHP array and stored in the `$posts` variable.

## Code explanation


- `wp_remote_get()`: This function makes an HTTP request to the specified URL and returns the response.
- `wp_remote_retrieve_body()`: This function retrieves the body of the response from the `wp_remote_get()` function.
- `json_decode()`: This function decodes a JSON string into a PHP array.

## Helpful links

- [WordPress REST API Handbook](https://developer.wordpress.org/rest-api/)
- [wp_remote_get()](https://developer.wordpress.org/reference/functions/wp_remote_get/)
- [wp_remote_retrieve_body()](https://developer.wordpress.org/reference/functions/wp_remote_retrieve_body/)
- [json_decode()](http://php.net/manual/en/function.json-decode.php)

onelinerhub: [How to use the WordPress REST API with PHP?](https://onelinerhub.com/php-wordpress/how-to-use-the-wordpress-rest-api-with-php)
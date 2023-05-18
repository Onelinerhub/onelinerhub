# How to create a custom field in WordPress using PHP?
// plain

Creating a custom field in WordPress using PHP is a relatively simple process. The following example code block will create a custom field with the name `my_custom_field` and the value `Hello World!`:

```
add_post_meta( $post_id, 'my_custom_field', 'Hello World!' );
```

The output of the above code will be a custom field with the name `my_custom_field` and the value `Hello World!` stored in the WordPress database.

## Code explanation


- `add_post_meta()`: This is the WordPress function used to create a custom field.
- `$post_id`: This is the ID of the post to which the custom field will be attached.
- `'my_custom_field'`: This is the name of the custom field.
- `'Hello World!'`: This is the value of the custom field.

## Helpful links

- [add_post_meta()](https://developer.wordpress.org/reference/functions/add_post_meta/)
- [Custom Fields in WordPress](https://www.wpbeginner.com/beginners-guide/custom-fields-wordpress/)

onelinerhub: [How to create a custom field in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-create-a-custom-field-in-wordpress-using-php)
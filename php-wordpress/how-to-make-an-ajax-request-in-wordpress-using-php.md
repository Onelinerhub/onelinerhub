# How to make an AJAX request in WordPress using PHP?
// plain

Making an AJAX request in WordPress using PHP is relatively easy. The following example code block shows how to make an AJAX request in WordPress using PHP:

```
add_action( 'wp_ajax_my_action', 'my_action_callback' );

function my_action_callback() {
	global $wpdb; // this is how you get access to the database

	$whatever = intval( $_POST['whatever'] );

	$whatever += 10;

        echo $whatever;

	wp_die(); // this is required to terminate immediately and return a proper response
}
```

The output of the example code is:

```
10
```

## Code explanation


1. `add_action( 'wp_ajax_my_action', 'my_action_callback' );` - This line adds an action hook to WordPress which will trigger the `my_action_callback` function when the AJAX request is made.

2. `function my_action_callback() {` - This line defines the `my_action_callback` function which will be triggered when the AJAX request is made.

3. `global $wpdb;` - This line allows access to the WordPress database.

4. `$whatever = intval( $_POST['whatever'] );` - This line retrieves the value of the `whatever` parameter from the AJAX request.

5. `$whatever += 10;` - This line adds 10 to the value of the `whatever` parameter.

6. `echo $whatever;` - This line prints the value of the `whatever` parameter.

7. `wp_die();` - This line is required to terminate the AJAX request and return a proper response.

## Helpful links

- [WordPress AJAX Tutorial](https://www.sitepoint.com/wordpress-ajax-tutorial/)
- [AJAX in Plugins](https://codex.wordpress.org/AJAX_in_Plugins)

onelinerhub: [How to make an AJAX request in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-make-an-ajax-request-in-wordpress-using-php)
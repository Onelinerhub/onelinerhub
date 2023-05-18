# How to add a shortcode in WordPress?
// plain

Adding a shortcode in WordPress is a great way to add custom functionality to your website. Shortcodes are small snippets of code that can be used to add dynamic content to your posts and pages.

To add a shortcode in WordPress, you need to first create a function that will generate the output for the shortcode. Here is an example of a simple shortcode that will display the current date:

```
function current_date_shortcode() {
    $date = date('F j, Y');
    return $date;
}
add_shortcode('current_date', 'current_date_shortcode');
```

This code will create a shortcode called `[current_date]` that will output the current date when used in a post or page.

The code consists of two parts:

1. The `current_date_shortcode()` function which generates the output for the shortcode.
2. The `add_shortcode()` function which registers the shortcode with WordPress.

Once the code is added to your theme's functions.php file, you can use the `[current_date]` shortcode in any post or page to display the current date.

## Helpful links

- [WordPress Shortcode API](https://developer.wordpress.org/reference/functions/add_shortcode/)
- [WordPress Shortcodes: A Complete Guide](https://www.wpbeginner.com/beginners-guide/wordpress-shortcodes-complete-guide/)

onelinerhub: [How to add a shortcode in WordPress?](https://onelinerhub.com/php-wordpress/how-to-add-a-shortcode-in-wordpress)
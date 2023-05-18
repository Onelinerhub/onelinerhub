# How to echo a shortcode in WordPress using PHP?
// plain

Echoing a shortcode in WordPress using PHP is a simple process. To do this, you can use the `do_shortcode()` function. This function takes a single parameter, which is the shortcode you want to echo.

For example, if you wanted to echo the shortcode `[my_shortcode]`, you would use the following code:
```
echo do_shortcode('[my_shortcode]');
```

The code above will output the shortcode `[my_shortcode]`.

The parts of the code are as follows:
- `echo`: This is a PHP command that prints out the result of the following expression.
- `do_shortcode()`: This is a WordPress function that takes a single parameter, which is the shortcode you want to echo.
- `'[my_shortcode]'`: This is the shortcode you want to echo.

## Helpful links
- [WordPress Codex - do_shortcode()](https://codex.wordpress.org/Function_Reference/do_shortcode)

onelinerhub: [How to echo a shortcode in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-echo-a-shortcode-in-wordpress-using-php)
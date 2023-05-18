# How to use hooks in WordPress with an example?
// plain

Hooks are a way to modify or add functionality to WordPress without editing core files. They are used to add custom code to WordPress.

## Example


```
add_action('init', 'my_custom_function');

function my_custom_function() {
    // Do something
}
```

This code will execute the function `my_custom_function` when the `init` hook is called.

## Code explanation


- `add_action`: This is a WordPress function that adds a custom function to a hook.
- `init`: This is the name of the hook that the custom function will be added to.
- `my_custom_function`: This is the name of the custom function that will be executed when the `init` hook is called.

## Helpful links

- [WordPress Hooks](https://developer.wordpress.org/plugins/hooks/)
- [add_action() Function](https://developer.wordpress.org/reference/functions/add_action/)

onelinerhub: [How to use hooks in WordPress with an example?](https://onelinerhub.com/php-wordpress/how-to-use-hooks-in-wordpress-with-an-example)
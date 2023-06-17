# How can I use jQuery in WordPress?
// plain

jQuery is a JavaScript library that provides a wide range of tools and functions for creating dynamic, interactive websites. It can be used in WordPress to create powerful and engaging user experiences.

To use jQuery in WordPress, you must first enqueue the script in your functions.php file. For example:

```
function my_scripts_method() {
    wp_enqueue_script(
        'custom-script',
        get_template_directory_uri() . '/js/custom_script.js',
        array('jquery')
    );
}
add_action('wp_enqueue_scripts', 'my_scripts_method');
```

This code will enqueue the custom_script.js file, which contains the jQuery code.

Once the script is enqueued, you can use it to manipulate the DOM, add event listeners, and create custom animations. For example:

```
$(document).ready(function() {
    $('.my-element').on('click', function() {
        $(this).animate({
            opacity: 0.5
        }, 500);
    });
});
```

This code will make the element with the class `my-element` fade to 50% opacity when clicked.

In addition to enqueuing and writing custom jQuery code, you can also use existing jQuery plugins in WordPress. To do this, you must first enqueue the plugin's script and then initialize it. For example:

```
wp_enqueue_script( 'my-plugin', get_template_directory_uri() . '/js/my_plugin.js', array('jquery') );

<script>
    jQuery(function($) {
        $('.my-element').myPlugin();
    });
</script>
```

This code will enqueue the my_plugin.js file and then initialize it on the element with the class `my-element`.

For more information on using jQuery in WordPress, see the [WordPress Codex](https://codex.wordpress.org/Using_Javascript).

onelinerhub: [How can I use jQuery in WordPress?](https://onelinerhub.com/jquery/how-can-i-use-jquery-in-wordpress)
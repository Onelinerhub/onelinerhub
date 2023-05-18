# How to create a WordPress plugin using PHP?
// plain

Creating a WordPress plugin using PHP is a relatively simple process. The following example code block will create a basic plugin that will display a message when activated:

```
<?php
/*
Plugin Name: My Plugin
Description: A basic plugin
*/

function my_plugin_function() {
    echo 'My plugin is now active!';
}

register_activation_hook(__FILE__, 'my_plugin_function');
```

When the plugin is activated, the following output will be displayed:

```
My plugin is now active!
```

The code consists of the following parts:

1. Plugin Name and Description: This is the name and description of the plugin that will be displayed in the WordPress admin area.

2. my_plugin_function(): This is the function that will be executed when the plugin is activated.

3. register_activation_hook(): This is the function that will register the my_plugin_function() to be executed when the plugin is activated.

## Helpful links

- [WordPress Plugin Development](https://developer.wordpress.org/plugins/)
- [register_activation_hook()](https://developer.wordpress.org/reference/functions/register_activation_hook/)

onelinerhub: [How to create a WordPress plugin using PHP?](https://onelinerhub.com/php-wordpress/how-to-create-a-wordpress-plugin-using-php)
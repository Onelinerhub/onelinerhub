# How to create a menu in WordPress using PHP?
// plain

Creating a menu in WordPress using PHP is a simple process. The following example code will create a menu in WordPress:

```
<?php
wp_nav_menu( array(
    'theme_location' => 'primary',
    'container' => false,
    'menu_class' => 'nav-menu'
) );
?>
```

This code will output a menu with the class `nav-menu`:

```
<ul class="nav-menu">
  <li><a href="#">Menu Item 1</a></li>
  <li><a href="#">Menu Item 2</a></li>
  <li><a href="#">Menu Item 3</a></li>
</ul>
```

The code consists of the following parts:

- `wp_nav_menu()`: This is the main function used to create a menu in WordPress.
- `theme_location`: This is the name of the menu location.
- `container`: This is a boolean value that determines whether a container element should be added around the menu.
- `menu_class`: This is the class that will be added to the menu.

For more information, please refer to the following links:

- [WordPress Codex - wp_nav_menu()](https://codex.wordpress.org/Function_Reference/wp_nav_menu)
- [WordPress Codex - Menus](https://codex.wordpress.org/WordPress_Menu_User_Guide)

onelinerhub: [How to create a menu in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-create-a-menu-in-wordpress-using-php)
# How to create a post in WordPress using PHP?
// plain

Creating a post in WordPress using PHP is a simple process. The following example code will create a post in WordPress using PHP:

```
$my_post = array(
  'post_title'    => 'My Post',
  'post_content'  => 'This is my post.',
  'post_status'   => 'publish',
  'post_author'   => 1
);

// Insert the post into the database
wp_insert_post( $my_post );
```

This code will create a post with the title "My Post" and the content "This is my post." The post will be published and the author will be the user with the ID of 1.

The code consists of the following parts:

1. An array containing the post data: `$my_post`
2. The `wp_insert_post()` function which inserts the post into the database

For more information, please refer to the [WordPress Codex](https://codex.wordpress.org/Function_Reference/wp_insert_post).

onelinerhub: [How to create a post in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-create-a-post-in-wordpress-using-php)
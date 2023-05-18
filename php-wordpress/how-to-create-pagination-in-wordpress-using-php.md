# How to create pagination in WordPress using PHP?
// plain

Pagination in WordPress can be created using PHP. It is a process of splitting content into multiple pages. The following example code can be used to create pagination in WordPress:

```
<?php
$paged = ( get_query_var( 'paged' ) ) ? get_query_var( 'paged' ) : 1;
$args = array(
    'posts_per_page' => 5,
    'paged' => $paged
);
$query = new WP_Query( $args );
?>
```

This code will output the following:

```
Array
(
    [posts_per_page] => 5
    [paged] => 1
)
```

The code consists of the following parts:

- `$paged`: This variable stores the page number of the current page.
- `get_query_var()`: This function retrieves the value of a query variable.
- `$args`: This array stores the arguments for the query.
- `posts_per_page`: This argument sets the number of posts to be displayed per page.
- `WP_Query()`: This function creates a new instance of WP_Query class.

## Helpful links

- [WP_Query Class](https://developer.wordpress.org/reference/classes/wp_query/)
- [Pagination in WordPress](https://www.wpbeginner.com/wp-tutorials/how-to-add-pagination-in-wordpress/)

onelinerhub: [How to create pagination in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-create-pagination-in-wordpress-using-php)
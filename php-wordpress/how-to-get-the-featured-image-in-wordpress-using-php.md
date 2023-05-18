# How to get the featured image in WordPress using PHP?
// plain

Getting the featured image in WordPress using PHP is a simple process. The following example code block will return the featured image URL of the current post:
```
<?php
$thumb_id = get_post_thumbnail_id();
$thumb_url = wp_get_attachment_image_src($thumb_id,'thumbnail-size', true);
echo $thumb_url[0];
?>
```
The output of the example code will be the URL of the featured image:
```
http://example.com/wp-content/uploads/featured-image.jpg
```
## Code explanation


1. `get_post_thumbnail_id()` - This function returns the post thumbnail ID.
2. `wp_get_attachment_image_src()` - This function returns an array of the image URL, width, height, and whether the image is an intermediate size.
3. `$thumb_url[0]` - This returns the URL of the featured image from the array.

## Helpful links

- [get_post_thumbnail_id()](https://developer.wordpress.org/reference/functions/get_post_thumbnail_id/)
- [wp_get_attachment_image_src()](https://developer.wordpress.org/reference/functions/wp_get_attachment_image_src/)

onelinerhub: [How to get the featured image in WordPress using PHP?](https://onelinerhub.com/php-wordpress/how-to-get-the-featured-image-in-wordpress-using-php)
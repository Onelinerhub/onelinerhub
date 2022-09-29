# How to save image in webp format

```php
$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagewebp($im, 'image.webp');
```




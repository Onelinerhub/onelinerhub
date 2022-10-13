# How to save image in webp format

```php
$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagewebp($im, '/tmp/image.webp');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imageellipse` - creates ellipse with specified coordinates, radius and border color
- `imagewebp` - saves given `gd` image in `webp` format to the specified path
- `/tmp/image.webp` - path to save image to

group: save_formats



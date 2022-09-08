# How to draw text with shadow

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$c_shadow = imageColorAllocate($im, 32,32,32);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 110, 110, $c_shadow, $font, 'Hi!');
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `$font` - path to `ttf` font to use
- `imagettftext` - draw text with given `ttf` font
- `40` - text font size
- `100, 100` - top left point to put text on
- `$c_green` - text color
- `'Hi!'` - text to draw
- `imagePng` - saves image in PNG format to the given path

group: text

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$c_shadow = imageColorAllocate($im, 32,32,32);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 110, 110, $c_shadow, $font, 'Hi!');
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


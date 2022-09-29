# How to change font size

```php
$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 55, 0, 50, 150, $c_green, $font, 'I am big');
imagettftext($im, 25, 0, 50, 50, $c_green, $font, 'I am small');

imagePng($im, '/tmp/image.png');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagettftext` - draw text with given `ttf` font
- `$font` - path to the font file
- `55` - larger font size
- `25` - smaller font size

group: font

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 50, 0, 50, 150, $c_green, $font, 'I am big');
imagettftext($im, 20, 0, 50, 50, $c_green, $font, 'I am small');

imagePng($im, '/tmp/image.png');
```


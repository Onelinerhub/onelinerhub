# How to use freetype font

### Before using freetype font, make sure your [GD library supports it](https://www.php.net/manual/en/image.installation.php).

```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/var/www/sumkin.otf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```

- `$font` - path to `freetype` font file (we used [sumkin](https://www.cufonfonts.com/font/sumkin-freetype) font for example)
- `imagettftext` - draw text with given `ttf` font

group: font

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/var/www/sumkin.otf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


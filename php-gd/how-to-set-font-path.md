# How to set font path

```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```

- `$font` - path to `ttf` font file
- `imagettftext` - draw text with given `ttf` font

group: font

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);
$c_green = imageColorAllocate($im, 46,204,64);

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
imagettftext($im, 40, 0, 100, 100, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


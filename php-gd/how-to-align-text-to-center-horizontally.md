# How to align text to center horizontally

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$text = 'Hi'

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
$p = imagettfbbox(40, 0, $font, $text);
print_r($p);

imagettftext($im, 40, 0, (400 - $p[2])/2, 100, $c_green, $font, $text);
```


group: text

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);
$text = 'Hi';

$font = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';
$p = imagettfbbox(40, 0, $font, $text);
print_r($p);

imagettftext($im, 40, 0, (400 - $p[2])/2, 100, $c_green, $font, $text);
imagePng($im, '/tmp/image.png');
```


# How to draw text

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagettftext($im, 20, 0, 50, 50, $c_green, $font, 'Hi!');

imagePng($im, '/tmp/image.png');
```


group: text



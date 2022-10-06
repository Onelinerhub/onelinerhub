# How to set background color

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_green = imageColorAllocate($im, 46,204,64);
imagefill($im, 0, 0, $c_green);

$c_black = imageColorAllocate($im, 0,0,0);
imageellipse($im, 200, 150, 100, 100, $c_black);

imagePng($im, '/tmp/image.png');
```




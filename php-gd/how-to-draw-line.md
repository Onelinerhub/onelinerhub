# How to draw line

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageline($im, 50, 50, 350, 250, $c_green);

imagePng($im, '/tmp/image.png');
```




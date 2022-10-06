# How to create transparent background

```php
<?php

$im = imagecreatetruecolor(400, 300);

imagealphablending($im, false);
$tr = imagecolorallocatealpha($im, 0, 0, 0, 127);
imagefill($im, 0, 0, $tr);
imagesavealpha($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
imagefilledellipse($im, 200, 150, 100, 100, $c_black);

imagePng($im, '/tmp/image.png');
```


group: background



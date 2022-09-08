# How to draw rectangle with border

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_fill = imageColorAllocate($im, 46,204,64);
$c_border = imageColorAllocate($im, 1,255,112);

imagefilledrectangle($im, 50, 100, 150, 200, $c_fill);
imagerectangle($im, 50, 100, 150, 200, $c_border);

imagePng($im, '/tmp/image.png');
```


group: rectangle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_fill = imageColorAllocate($im, 46,204,64);
$c_border = imageColorAllocate($im, 1,255,112);

imagefilledrectangle($im, 50, 100, 150, 200, $c_fill);
imagerectangle($im, 50, 100, 150, 200, $c_border);

imagePng($im, '/tmp/image.png');
```


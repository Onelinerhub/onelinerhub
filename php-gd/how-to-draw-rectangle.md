# How to draw rectangle

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagerectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```


group: rectangle

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagerectangle($im, 50, 100, 150, 200, $c_green);

imagePng($im, '/tmp/image.png');
```


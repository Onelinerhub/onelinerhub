# Convert GD output to base64

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 80, 80, $c_green);

ob_start();
imagePng($im);
$base_64 = base64_encode(ob_get_clean());
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagefilledellipse` - creates ellipse with specified coordinates, radius and color
- `ob_start()` - start output buffering
- `imagePng($im)` - output `$im` image in `PNG` format
- `ob_get_clean()` - return contents of output buffer (and clean it after that)
- `$base_64` - will contain base64-encoded image

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);
imageantialias($im, true);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 80, 80, $c_green);

ob_start();
imagePng($im);
$base_64 = base64_encode(ob_get_clean());
echo $base_64;
```
```
iVBORw0KGgoAAAANSUhEUgAAA...
```


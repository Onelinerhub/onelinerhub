# How to output image to browser

```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

ob_start();
imagejpeg($im, null, 95);
$data = ob_get_clean();

echo "<img src='data:image/jpeg;base64," . base64_encode( $data ) . "' />";
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imageellipse` - creates ellipse with specified coordinates, radius and border color
- `ob_start()` - start buffering output (instead of outputting)
- `imagejpeg` - saves image as JPEG (returns data if second argument is null, as in our case)
- `ob_get_clean()` - returns buffered content (image data in our case)
- `data:image/jpeg;base64,` - allows us to use image data string in `src` attribute instead of path to file



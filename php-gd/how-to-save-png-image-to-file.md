# How to save PNG image to file

```php
$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagepng($im, '/tmp/image.png');
```

- `imagepng` - saves given image resource in `PNG` format

group: save_formats

## Example: 
```php
<?php

$im = imagecreatetruecolor(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imageellipse($im, 200, 150, 100, 100, $c_green);

imagepng($im, '/tmp/image.png');
```


# Draw bar chart

```php
<?php

$data = [10, 40, 20, 60, 80, 75];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

$c_green = imageColorAllocate($im, 46,204,64);
foreach ( $data as $i => $v ) {
  imagefilledrectangle($im, ($i + 1) * 50, 250 - $v, ($i + 1) * 50 + 40, 250, $c_green);
}

imagePng($im, '/tmp/image.png');
```

- `$data` - example data to draw bar chart based on
- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to later use in image
- `imagefilledrectangle` - creates filled rectangle
- `imagePng` - saves image in PNG format to the given path

group: chart

## Example: 
```php
<?php

$data = [10, 40, 20, 60, 80, 75];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

$c_green = imageColorAllocate($im, 46,204,64);
foreach ( $data as $i => $v ) {
  imagefilledrectangle($im, ($i + 1) * 50, 250 - $v, ($i + 1) * 50 + 40, 250, $c_green);
}

imagePng($im, '/tmp/image.png');
```


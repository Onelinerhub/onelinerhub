# How to draw pie chart

```php
<?php

$data = [50, 90, 150, 360];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

foreach ( $data as $i => $v ) {
  $c = imageColorAllocate($im, 46 + $i * 30,204 - $i * 30, 64 + $i * 30);
  imagefilledarc(
    $im, 200, 150,
    100 + $i * 10, 100 + $i * 10, $i ? $data[$i-1] : 0,
    $v, $c, IMG_ARC_PIE
  );
}

imagePng($im, '/tmp/image.png');
```

- `$data` - sample data to draw pie chart based on
- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imageColorAllocate` - creates color object to use for pie (we use `$i` value to randomize color)
- `imagefilledarc` - draw next pie
- `200, 150` - pie center coordinates
- `imagePng` - saves image in PNG format to the given path

group: chart

## Example: 
```php
<?php

$data = [50, 90, 150, 360];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

foreach ( $data as $i => $v ) {
  $c_green = imageColorAllocate($im, 46 + $i * 30,204 - $i * 30, 64 + $i * 30);
  imagefilledarc($im, 200, 150, 100 + $i * 10, 100 + $i * 10, $i ? $data[$i-1] : 0, $v, $c_green, IMG_ARC_PIE);
}

imagePng($im, '/tmp/image.png');
```


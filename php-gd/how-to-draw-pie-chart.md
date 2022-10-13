# How to draw pie chart

```php
<?php

$data = [50, 90, 150, 70];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

foreach ( $data as $i => $v ) {
  $c_green = imageColorAllocate($im, 46 + $i * 10,204,64);
  imagefilledarc($im, 200, 150, 100, 100, $i ? $data[$i-1] : 0, $v, $c_green, IMG_ARC_PIE);
}

imagePng($im, '/tmp/image.png');
```


group: chart

## Example: 
```php
<?php

$data = [50, 90, 150, 70];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

foreach ( $data as $i => $v ) {
  $c_green = imageColorAllocate($im, 46 + $i * 10,204,64);
  imagefilledarc($im, 200, 150, 100, 100, $i ? $data[$i-1] : 0, $v, $c_green, IMG_ARC_PIE);
}

imagePng($im, '/tmp/image.png');
```


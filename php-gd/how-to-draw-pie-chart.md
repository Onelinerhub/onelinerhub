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


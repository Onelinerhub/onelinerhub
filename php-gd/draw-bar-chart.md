# Draw bar chart

```php
<?php

$data = [10, 40, 20, 60, 80];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

$c_green = imageColorAllocate($im, 46,204,64);
foreach ( $data as $i => $v ) {
  imagefilledrectangle($im, $i * 50, 250 - $v, $i * 50 + 40, 250, $c_green);
}

imagePng($im, '/tmp/image.png');
```


group: chart

## Example: 
```php
<?php

$data = [10, 40, 20, 60, 80];

$im = imagecreatetruecolor(400, 300);
$c_black = imageColorAllocate($im, 0,0,0);

$c_green = imageColorAllocate($im, 46,204,64);
foreach ( $data as $i => $v ) {
  imagefilledrectangle($im, $i * 50, 250 - $v, $i * 50 + 40, 250, $c_green);
}

imagePng($im, '/tmp/image.png');
```


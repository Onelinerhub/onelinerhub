# How to draw circle

```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```


group: circle

## Example: 
```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($im, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

imagePng($im, '/tmp/image.png');
```


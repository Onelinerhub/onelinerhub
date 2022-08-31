# Using GD example 

```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($image, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

header("Content-type: image/png");
imagePng($im);
imageDestroy($im);
```


group: install

## Example: 
```php
<?php

$im = imageCreate(400, 300);

$c_black = imageColorAllocate($im, 0,0,0);
$c_green = imageColorAllocate($image, 46,204,64);

imagefilledellipse($im, 200, 150, 100, 100, $c_green);

header("Content-type: image/png");
imagePng($im);
imageDestroy($im);
```
```
124
```


# How to get image size from resource

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$width  = imagesx($im);
$height = imagesy($im);
```

- `$im` - image resource to get size of
- `imagesx` - returns width of given image
- `imagesy` - returns height of given image

group: size

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);
$im = imagecreatefrompng($file);

$width  = imagesx($im);
$height = imagesy($im);

echo $width . 'x' . $height;
```
```
733x1100
```


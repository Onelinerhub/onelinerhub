# How to get image size

```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);

$width = $size[0];
$height = $size[1];

```

- `/var/www/examples/heroine.png` - path to image to get size of
- `getimagesize` - returns image size from given path
- `$width` - will contain image width
- `$height` - will contain image height

group: size

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$size = getimagesize($file);

$width = $size[0];
$height = $size[1];

echo $width . 'x' . $height;
```
```
733x1100
```


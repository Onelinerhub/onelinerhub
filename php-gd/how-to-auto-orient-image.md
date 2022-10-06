# How to auto orient image

### We can use `EXIF` data to get image orientation (in case it has this data set):

```php
<?php

$file = 'source.jpg';
$im = imagecreatefromjpeg($file);

$rotation = [0, 0, 0, 180, 0, 0, -90, 0, 90][@exif_read_data($file)['COMPUTED']['Orientation'] ?: 0];
if ( $rotation ) {
  $im = imagerotate($im, $rotation, 0);
}

imagejpeg($im, 'result.jpg');
```

- `$file` - source image file to auto orient
- `imagecreatefromjpeg` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `exif_read_data` - returns `EXIF` data of a specified image
- `$rotation` - define rotation angle accordingly to image orientation
- `imagerotate` - rotates `$im` image by `$rotation`
- `imagejpeg` - save given image to the given `JPEG` file

group: orient



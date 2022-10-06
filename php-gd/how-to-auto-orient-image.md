# How to auto orient image

### We can use `EXIF` data to get image orientation (in case it has this data set):

```php
<?php

$file = 'source.png';
$im = imagecreatefrompng($file);

$rotation = [0, 0, 0, 180, 0, 0, -90, 0, 90][@exif_read_data($file)['Orientation'] ?: 0];
if ( $rotation ) {
  $im = imagerotate($im, $rotation, 0);
}

imagepng($im, 'result.png');
```

- `exif_read_data` - returns `EXIF` data of a specified image
- `['COMPUTED']['Orientation']` - get orientation value from `EXIF` data
- `$orientation` - will contain [orientation value](http://sylvana.net/jpegcrop/exif_orientation.html)

group: orient



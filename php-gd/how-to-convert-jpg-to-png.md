# How to convert jpg to png

```php
<?php

$im = imagecreatefromjpeg('image.jpg');
imagepng($im, 'result.png');
```

- `imagecreatefromjpeg` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagepng` - saves given image resource in `PNG` format

group: convert



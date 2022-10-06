# How to convert jpg to webp

```php
<?php

$im = imagecreatefromjpeg('image.jpg');
imagewebp($im, '/tmp/image.webp');
```

- `imagecreatefromjpeg` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagewebp` - saves given `gd` image in `webp` format to the specified path

group: convert



# How to convert png to jpg

```php
<?php

$im = imagecreatefrompng('image.png');
imagejpeg($im, '/tmp/image.jpg');
```

- `imagejpeg` - saves given `gd` image in `jpeg` format to the specified path
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image

group: convert



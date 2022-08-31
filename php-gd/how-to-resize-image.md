# How to resize image

```php
<?php

$im = imagecreatefrompng('/var/www/examples/heroine.png');

$imf = imagecreatetruecolor(400, 300);
imagecopyresampled($imf, $im, 0,0,0,0, 400,300,4000,3000);

imagePng($imf, '/tmp/image.png');
```


group: resize



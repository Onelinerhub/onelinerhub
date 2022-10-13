# How to get pixel color

```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);
$c = imagecolorat($im, 50, 50);
```




# How to get pixel color

```php
$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);
$c = imagecolorat($im, 50, 50);
```


## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);
$c = imagecolorat($im, 50, 50);

echo $c;
```
```
515
```


# How to get pixel color

```php
$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);
$c = imagecolorat($im, 100, 100);
list($r, $g, $b) = [($c >> 16) & 0xFF, ($c >> 8) & 0xFF, $c & 0xFF];
```

- `$file` - sample image to work with
- `imagecreatefrompng` - creates [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object from given PNG image
- `imagecolorat` - returns color at a given position as an integer
- `100, 100` - we're getting color on `100` pixels from top and `100` pixels from left
- `$r, $g, $b` - variables will contain decoded values for `R`, `G` and `B` color channels

## Example: 
```php
<?php

$file = '/var/www/examples/heroine.png';
$im = imagecreatefrompng($file);
$c = imagecolorat($im, 100, 100);
list($r, $g, $b) = [($c >> 16) & 0xFF, ($c >> 8) & 0xFF, $c & 0xFF];

echo $r . ' ' . $g . ' ' . $b;
```
```
186 194 168
```


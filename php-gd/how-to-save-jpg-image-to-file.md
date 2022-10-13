# How to save JPG image to file

```php
$im = imagecreatetruecolor(400, 300);

# ...

imagejpeg($im, '/tmp/image.jpg');
```

- `imagecreatetruecolor` - creates true color [lib:GD](https://onelinerhub.com/php-gd/how-to-install-gd-for-php-on-ubuntu-ubuntuversion) image object with specified width & height
- `imagejpeg` - saves `$im` gd object to the specified 'jpeg' file
- `/tmp/image.jpg` - path to save `jpeg` to

group: save_formats



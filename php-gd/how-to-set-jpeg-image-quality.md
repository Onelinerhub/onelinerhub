# How to set jpeg image quality

```php
# ...

imagejpeg($im, '/tmp/image.jpg', 90);
```

- `imagejpeg` - saves `$im` gd object to the specified 'jpeg' file
- `/tmp/image.jpg` - path to save `jpeg` to
- `90` - level of image quality (use `100` for best quality, lower values reduce quality)

group: quality



# How to get image type

```php
$file = '/path/to/image';
$data = getimagesizefromstring(file_get_contents($file));
$type = $data['mime'];
```

- `$file` - path to image of unknown type
- `getimagesizefromstring` - returns image meta data from given string
- `file_get_contents` - reads given file

## Example: 
```php
<?php

$file = '/path/to/image';
$data = getimagesizefromstring(file_get_contents($file));

echo $data['mime'];
```
```
image/jpeg
```


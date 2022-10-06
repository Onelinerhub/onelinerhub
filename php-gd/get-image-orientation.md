# Get image orientation

### We can use `EXIF` data to get image orientation (in case it has this data set):

```php
<?php

$orientation = exif_read_data('photo.jpg')['COMPUTED']['Orientation'];
```

- `exif_read_data` - returns `EXIF` data of a specified image
- `['COMPUTED']['Orientation']` - get orientation value from `EXIF` data
- `$orientation` - will contain [orientation value](http://sylvana.net/jpegcrop/exif_orientation.html)

group: orient



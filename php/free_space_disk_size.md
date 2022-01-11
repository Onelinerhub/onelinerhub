# Get free space on disk

```php
$bytes = disk_free_space('/');
```

- `disk_free_space` - returns free disk space in bytes for specified disk partition
- `'/'` - get free space for root partition

## Example: 
```php
<?php

echo disk_free_space('.');
```
```
13619806208
```


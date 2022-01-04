# Remove a directory that is not empty

```php
function deleteDirectory($dir) {
	system('rm -rf — ' . escapeshellarg($dir), $retval);
	return $retval == 0;
}

deleteDirectory("foldername");
```
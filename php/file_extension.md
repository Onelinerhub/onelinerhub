# Get file extension

```php
$ext = pathinfo($file_name, PATHINFO_EXTENSION);
```

- $ext - extension will be placed here
- pathinfo - function to get [parts of file path](https://www.php.net/manual/function.pathinfo.php)
- $file_name - name of the file to get extension for
- PATHINFO_EXTENSION - will ask `pathinfo` function to return extension only

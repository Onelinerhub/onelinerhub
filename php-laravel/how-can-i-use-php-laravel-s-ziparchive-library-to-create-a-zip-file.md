# How can I use PHP Laravel's ZipArchive library to create a zip file?
// plain

To use the ZipArchive library to create a zip file in PHP Laravel, you can take the following steps:

1. Include the ZipArchive library with the following code:
```
use ZipArchive;
```

2. Create a new ZipArchive object:
```
$zip = new ZipArchive;
```

3. Create a new zip file:
```
$zip->open('my_zip_file.zip', ZipArchive::CREATE);
```

4. Add files to the zip file:
```
$zip->addFile('file1.txt');
$zip->addFile('file2.txt');
```

5. Close the zip file:
```
$zip->close();
```

6. Verify the zip file was created:
```
if ($zip->open('my_zip_file.zip') === TRUE) {
    echo 'Zip file created successfully!';
    $zip->close();
}
```

7. Output:
```
Zip file created successfully!
```

## Helpful links
- [ZipArchive Documentation](https://www.php.net/manual/en/class.ziparchive.php)
- [Laravel Documentation](https://laravel.com/docs/7.x)

onelinerhub: [How can I use PHP Laravel's ZipArchive library to create a zip file?](https://onelinerhub.com/php-laravel/how-can-i-use-php-laravel-s-ziparchive-library-to-create-a-zip-file)
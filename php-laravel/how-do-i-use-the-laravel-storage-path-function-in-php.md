# How do I use the Laravel storage_path function in PHP?
// plain

The `storage_path()` function in Laravel is used to get the fully qualified path to the storage directory of the application. This directory is used to store files and other persistent data.

## Example code

```
$storagePath = storage_path();
echo $storagePath;
```
## Output example

```
/var/www/html/storage
```

The code above will get the storage directory path and store it in the `$storagePath` variable. Then it will echo the path to the console.

The parts of the code are:
- `storage_path()` - this is the function used to get the storage path
- `$storagePath` - this is the variable used to store the storage path
- `echo $storagePath` - this is used to echo the storage path to the console

## Helpful links
- [Laravel Documentation - Filesystem](https://laravel.com/docs/5.8/filesystem)
- [Laravel Documentation - Helpers](https://laravel.com/docs/5.8/helpers#method-storage-path)

onelinerhub: [How do I use the Laravel storage_path function in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-the-laravel-storage-path-function-in-php)
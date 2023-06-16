# How can I use Laravel Storage to store files in PHP?
// plain

Laravel Storage is a powerful tool that allows you to store files in PHP. You can use the `Storage` facade to access files within the `storage` directory.

## Example code

```
$file = Storage::put('my_file.txt', 'Hello World!');
```

This will create a file `my_file.txt` in the `storage` directory with the content `Hello World!`.

## Code explanation


1. `Storage`: This is the facade that allows you to access files within the `storage` directory.
2. `put()`: This is a method of the `Storage` facade that allows you to create a new file.
3. `my_file.txt`: This is the name of the file that will be created.
4. `Hello World!`: This is the content of the file that will be created.

## Helpful links

- [Laravel Storage Documentation](https://laravel.com/docs/7.x/filesystem)
- [Laravel Storage Facade Documentation](https://laravel.com/api/7.x/Illuminate/Contracts/Filesystem/Storage.html)

onelinerhub: [How can I use Laravel Storage to store files in PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-laravel-storage-to-store-files-in-php)
# How do I upload a file using PHP and Laravel?
// plain

To upload a file using PHP and Laravel, you can use the `request()->file('file')` method. This method takes the name of the file from the form field and stores it in the `$file` variable.

## Example code

```
$file = request()->file('file');
```

The file can then be stored using the `Storage::put()` method. This method takes two parameters, the first being the path to the file and the second being the file itself.

## Example code

```
Storage::put('file.txt', $file);
```

The file can also be moved to a different location using the `Storage::move()` method. This method takes three parameters, the first being the path to the file, the second being the new path and the third being the file itself.

## Example code

```
Storage::move('file.txt', 'new-file.txt', $file);
```

## Helpful links

* [Laravel Docs - File Storage](https://laravel.com/docs/7.x/filesystem#file-storage)
* [Laravel Docs - Request](https://laravel.com/docs/7.x/requests#retrieving-uploaded-files)

onelinerhub: [How do I upload a file using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-upload-a-file-using-php-and-laravel)
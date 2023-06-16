# How can I use the PHP Zipstream library in a Laravel project?
// plain

The [PHP Zipstream library](https://github.com/Grandt/PHPZip) can be used in a Laravel project to create and stream archives on-the-fly. It is a lightweight alternative to the [ZipArchive](https://www.php.net/manual/en/class.ziparchive.php) class for creating ZIP files.

To begin, you'll need to install the library using Composer.

```
composer require grandt/phpzip
```

Once the library is installed, you can use it in your Laravel project. For example, to create a ZIP file containing files from the `storage/app/public` directory:

```php
use Grandt\PhpZip\ZipFile;

$zip = new ZipFile();
$zip->addDirectoryContent('storage/app/public');
$zip->outputAsAttachment('files.zip');
```

The output of the code above would be a ZIP file called `files.zip` containing the contents of the `storage/app/public` directory.

You can also add files to the archive from other sources. For example, to add a file from an URL:

```php
$zip->addFileFromUrl('http://example.com/file.txt', 'file.txt');
```

You can find more information about the library and its features in the [PHP Zipstream library documentation](https://github.com/Grandt/PHPZip/blob/master/README.md).

onelinerhub: [How can I use the PHP Zipstream library in a Laravel project?](https://onelinerhub.com/php-laravel/how-can-i-use-the-php-zipstream-library-in-a-laravel-project)
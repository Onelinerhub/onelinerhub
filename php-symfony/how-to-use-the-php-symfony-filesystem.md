# How to use the PHP Symfony filesystem?
// plain

The Symfony Filesystem component provides basic utilities for manipulating the file system. It provides methods for creating, reading, writing, and deleting files and directories.

## Example code

```
use Symfony\Component\Filesystem\Filesystem;

$fs = new Filesystem();

// Create a directory
$fs->mkdir('/path/to/directory');

// Copy a file
$fs->copy('/path/to/source/file.txt', '/path/to/destination/file.txt');

// Check if a file exists
if ($fs->exists('/path/to/file.txt')) {
    // Do something
}
```

The code above creates a directory, copies a file, and checks if a file exists.

## Code explanation


- `use Symfony\Component\Filesystem\Filesystem;`: This imports the Filesystem class from the Symfony Filesystem component.

- `$fs = new Filesystem();`: This creates a new instance of the Filesystem class.

- `$fs->mkdir('/path/to/directory');`: This creates a directory at the specified path.

- `$fs->copy('/path/to/source/file.txt', '/path/to/destination/file.txt');`: This copies a file from the source path to the destination path.

- `if ($fs->exists('/path/to/file.txt')) {`: This checks if a file exists at the specified path.

## Helpful links

- [Symfony Filesystem Component Documentation](https://symfony.com/doc/current/components/filesystem.html)

onelinerhub: [How to use the PHP Symfony filesystem?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-filesystem)
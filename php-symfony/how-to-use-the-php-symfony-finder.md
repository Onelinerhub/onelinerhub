# How to use the PHP Symfony Finder?
// plain

The PHP Symfony Finder is a powerful tool for searching through directories and files. It can be used to locate files and directories based on a variety of criteria.

## Example

```
$finder = new Symfony\Component\Finder\Finder();
$finder->files()->name('*.txt')->in('/path/to/dir');

foreach ($finder as $file) {
    // do something with the file
}
```

The code above will search for all files with the .txt extension in the specified directory.

The Finder class provides a variety of methods for searching through directories and files. These include:

- `files()`: Search for files
- `directories()`: Search for directories
- `name()`: Search for files or directories with a specific name
- `in()`: Search in a specific directory
- `contains()`: Search for files or directories containing a specific string
- `notName()`: Search for files or directories not having a specific name
- `notContains()`: Search for files or directories not containing a specific string

## Helpful links
- [Symfony Finder Documentation](https://symfony.com/doc/current/components/finder.html)
- [GitHub Repository](https://github.com/symfony/finder)

onelinerhub: [How to use the PHP Symfony Finder?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-finder)
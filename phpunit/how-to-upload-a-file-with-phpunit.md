# How to upload a file with PHPUnit?
// plain

PHPUnit provides a way to upload files using the [`setUploadFiles`](https://phpunit.readthedocs.io/en/9.2/api.html#phpunit-framework-constraint-file-setuploadfiles) method. This method takes an array of file paths and sets them as the files to be uploaded.

## Example code

```php
$files = [
    'file1.txt' => 'file1.txt',
    'file2.txt' => 'file2.txt'
];

$request = new \Symfony\Component\HttpFoundation\Request();
$request->files->setUploadFiles($files);
```

## Output example

```
null
```

## Code explanation

- `$files`: An array of file paths to be uploaded.
- `$request`: An instance of the Symfony `Request` class.
- `setUploadFiles`: The method used to set the files to be uploaded.

## Helpful links
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/9.2/index.html)
- [Symfony Request Class](https://symfony.com/doc/current/components/http_foundation/introduction.html#the-request-class)
# How do I use PHP and Elastica to zip a file?
// plain

Using PHP and Elastica to zip a file is a fairly straightforward process. Here is an example code block to demonstrate:

```php
<?php
// Include the Elastica library
require_once 'vendor/autoload.php';

// Create a new instance of the ZipArchive class
$zip = new ZipArchive();

// Open the zip file for writing
$zip->open('my_archive.zip', ZipArchive::CREATE);

// Add the file to the zip
$zip->addFile('my_file.txt');

// Close the zip
$zip->close();
?>
```

This code will create a zip file called `my_archive.zip` that contains the file `my_file.txt`.

The code consists of the following parts:

1. Include the Elastica library - This includes the Elastica library, which is required to use the ZipArchive class.
2. Create a new instance of the ZipArchive class - This creates a new instance of the ZipArchive class.
3. Open the zip file for writing - This opens the zip file for writing.
4. Add the file to the zip - This adds the file to the zip.
5. Close the zip - This closes the zip.

For more information, see the [Elastica documentation](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/zip_archive.html).

onelinerhub: [How do I use PHP and Elastica to zip a file?](https://onelinerhub.com/php-elastica/how-do-i-use-php-and-elastica-to-zip-a-file)
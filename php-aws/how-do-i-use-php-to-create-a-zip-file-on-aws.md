# How do I use PHP to create a ZIP file on AWS?
// plain

Creating a ZIP file on AWS using PHP is a relatively simple process. The following example code block will demonstrate how to create a ZIP file using PHP:

```
// Create a new ZIP file
$zip = new ZipArchive;

// Open the ZIP file
if ($zip->open('test.zip', ZipArchive::CREATE) === TRUE) {
    // Add a file to the ZIP file
    $zip->addFile('test.txt');
    // Close the ZIP file
    $zip->close();
    echo 'Successfully created the ZIP file!';
} else {
    echo 'Failed to create the ZIP file.';
}
```

## Output example
 `Successfully created the ZIP file!`

## Code explanation

1. `$zip = new ZipArchive;`: This creates a new ZipArchive object.
2. `if ($zip->open('test.zip', ZipArchive::CREATE) === TRUE) {`: This opens the ZIP file for writing and returns true if successful.
3. `$zip->addFile('test.txt');`: This adds the file `test.txt` to the ZIP file.
4. `$zip->close();`: This closes the ZIP file.

## Helpful links
- [PHP ZipArchive](https://www.php.net/manual/en/class.ziparchive.php)
- [Creating a ZIP File](https://www.php.net/manual/en/zip.examples.php#example-4642)

onelinerhub: [How do I use PHP to create a ZIP file on AWS?](https://onelinerhub.com/php-aws/how-do-i-use-php-to-create-a-zip-file-on-aws)
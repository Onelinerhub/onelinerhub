# How do I use PHP Omnipay to create a zip file?
// plain

To create a zip file using PHP Omnipay, you must first install the library. This can be done by running the following command in your terminal:

```
composer require league/omnipay
```

Once installed, you can use the following code block to create a zip file:

```
<?php

require 'vendor/autoload.php';

$omnipay = new \Omnipay\Omnipay();
$zip = $omnipay->create('Zip');

$zip->addFile('file1.txt');
$zip->addFile('file2.txt');

$zip->saveAs('files.zip');
```

The code above will create a zip file named `files.zip` containing the two files `file1.txt` and `file2.txt`.

The code consists of the following parts:

- `require 'vendor/autoload.php';`: This loads the Omnipay library.
- `$omnipay = new \Omnipay\Omnipay();`: This creates a new Omnipay instance.
- `$zip = $omnipay->create('Zip');`: This creates a new Zip instance.
- `$zip->addFile('file1.txt');`: This adds the file `file1.txt` to the zip file.
- `$zip->addFile('file2.txt');`: This adds the file `file2.txt` to the zip file.
- `$zip->saveAs('files.zip');`: This saves the zip file as `files.zip`.

For more information, please refer to the [Omnipay documentation](https://omnipay.thephpleague.com/).

onelinerhub: [How do I use PHP Omnipay to create a zip file?](https://onelinerhub.com/php-omnipay/how-do-i-use-php-omnipay-to-create-a-zip-file)
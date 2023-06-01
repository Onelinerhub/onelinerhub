# How can I use AWS Textract with PHP?
// plain

Using AWS Textract with PHP requires the [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/).

Once installed, you can use the AWS SDK to call the Textract API. For example, the following code will detect text from an image file:

```php
<?php

require 'vendor/autoload.php';

use Aws\Textract\TextractClient;

$textract = new TextractClient([
    'region' => 'us-east-1',
    'version' => '2018-06-27'
]);

$result = $textract->detectDocumentText([
    'Document' => [
        'Bytes' => file_get_contents('image.jpg')
    ]
]);

print_r($result);
```

The output of this code will be an array containing the detected text from the image.

The code can also be used to detect text from PDFs. To do this, the PDF will need to be converted to a byte array first.

```php
<?php

require 'vendor/autoload.php';

use Aws\Textract\TextractClient;

$textract = new TextractClient([
    'region' => 'us-east-1',
    'version' => '2018-06-27'
]);

$pdf_bytes = file_get_contents('document.pdf');

$result = $textract->detectDocumentText([
    'Document' => [
        'Bytes' => $pdf_bytes
    ]
]);

print_r($result);
```

The output of this code will be an array containing the detected text from the PDF.

For more information, see the [AWS Textract Documentation](https://docs.aws.amazon.com/textract/latest/dg/API_Operations.html).

onelinerhub: [How can I use AWS Textract with PHP?](https://onelinerhub.com/php-aws/how-can-i-use-aws-textract-with-php)
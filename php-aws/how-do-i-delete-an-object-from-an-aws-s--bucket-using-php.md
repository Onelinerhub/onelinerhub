# How do I delete an object from an AWS S3 bucket using PHP?
// plain

To delete an object from an AWS S3 bucket using PHP, you can use the AWS SDK for PHP.

First, you need to install the AWS SDK for PHP. To do this, you can use the Composer dependency manager.

```
composer require aws/aws-sdk-php
```

Once the SDK is installed, you can use the `deleteObject()` method in the `Aws\S3\S3Client` class to delete an object from an S3 bucket.

```
<?php

require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ],
]);

$s3->deleteObject([
    'Bucket' => 'my-bucket',
    'Key'    => 'my-object',
]);
```

The `deleteObject()` method takes an array of parameters, including the `Bucket` and `Key` parameters to specify the bucket and object to delete.

For more information on deleting objects from S3 buckets using PHP with the AWS SDK, see the [Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.S3.S3Client.html#_deleteObject).

onelinerhub: [How do I delete an object from an AWS S3 bucket using PHP?](https://onelinerhub.com/php-aws/how-do-i-delete-an-object-from-an-aws-s--bucket-using-php)
# How can I use PHP to list objects stored in AWS S3?
// plain

Using PHP, you can list objects stored in AWS S3 by using the [listObjectsV2](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#listobjectsv2) method from the AWS SDK for PHP.

The following example code will list all objects stored in an S3 bucket:

```php
<?php

require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3 = new S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);

$objects = $s3->listObjectsV2([
    'Bucket' => 'YOUR_S3_BUCKET_NAME'
]);

foreach ($objects['Contents'] as $object) {
    echo $object['Key'] . PHP_EOL;
}

```

This example code will output the name of each object stored in the S3 bucket:

```
object1.txt
object2.txt
object3.txt
```

The code is broken down into the following parts:

1. Require the autoloader from the AWS SDK for PHP: `require 'vendor/autoload.php';`
2. Use the S3Client class from the AWS SDK for PHP: `use Aws\S3\S3Client;`
3. Create a new S3Client instance with your AWS credentials:
```php
$s3 = new S3Client([
    'region'  => 'us-west-2',
    'version' => 'latest',
    'credentials' => [
        'key'    => 'YOUR_AWS_ACCESS_KEY_ID',
        'secret' => 'YOUR_AWS_SECRET_ACCESS_KEY',
    ]
]);
```
4. List the objects in the S3 bucket using the `listObjectsV2` method:
```php
$objects = $s3->listObjectsV2([
    'Bucket' => 'YOUR_S3_BUCKET_NAME'
]);
```
5. Iterate over the list of objects and output the name of each object:
```php
foreach ($objects['Contents'] as $object) {
    echo $object['Key'] . PHP_EOL;
}
```

## Helpful links
- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/aws-sdk-php/v3/api/index.html)
- [listObjectsV2](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-s3-2006-03-01.html#listobjectsv2)

onelinerhub: [How can I use PHP to list objects stored in AWS S3?](https://onelinerhub.com/php-aws/how-can-i-use-php-to-list-objects-stored-in-aws-s-)